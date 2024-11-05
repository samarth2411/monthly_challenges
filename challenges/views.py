from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Jan Challenge",
    "february": "Feb Challenge",
    "march": "March Challenge",
    "april": "April Challenge",
    "may": "May Challenge",
    "june": "June Challenge",
    "july": "July Challenge",
    "august": "August Challenge",
    "september": "September Challenge",
    "october": "October Challenge",
    "november": "November Challenge",
    "december": "December Challenge",
}


def monthly_challenges_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month<h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])   # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}<h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported<h1>")
