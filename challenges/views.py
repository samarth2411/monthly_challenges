from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges_data = {
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

def index(request):
    # list_items = ""
    months = list(monthly_challenges_data.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
    # for month in months:
    #     capatilized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capatilized_month}</a></li>"
    
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

def monthly_challenges_number(request, month):
    months = list(monthly_challenges_data.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])   # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_data[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month.capitalize()
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
