from urllib import response
from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthlyList={
    "january":"Create a list of sub-tasks",
    "february":"walk for 20 minutes",
    "march":"Eat no meat for the entire month",
    "april":"Travel more",
    "may":"Read more",
    "june":"Quit smoking",
    "july":"Learn a new skill or hobby ",
    "august":"Lose weight",
    "september":"Exercise more",
    "october":"Spend more time with family and friends",
    "novemeber":"Save more money ",
    "december":None
}

def index(request):
    months= list(monthlyList.keys())

    return render(request,"challenges/index.html",{
        "months":months
    })
    #for month in months:
    #     capitalizedMonth=month.capitalize()
    #     redirectPath=reverse("monthChallenge",args=[month])#challenges
    #     listItems+=f"""<li><a href="{redirectPath}">{capitalizedMonth}</a></li>"""
    #
    #resp=f"<ul>{listItems}</ul>"
    #return HttpResponse(resp)


def monthly_challenge_by_number(request,month):
    months=list(monthlyList.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not supported")
    forwardMonth=months[month-1]
    redirectPath=reverse("monthChallenge",args=[forwardMonth])#challenges
    return HttpResponseRedirect(redirectPath)

def monthly_challenge(request,month):
    print(request)
    try:
        challengeText=monthlyList[month]
        #responseData=f"<h1>{challengeText}</h1>"
        #responseData=render_to_string("challenges/challenge.html")
        #return HttpResponse(responseData)

        return render(request,"challenges/challenge.html",{"text":challengeText,
                                                           "monthName":month
                                                            })
    except:
        raise Http404()
        #render_to_string("404.html")
        #return HttpResponseNotFound(render_to_string)
    