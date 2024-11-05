from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# def jan(request):
#     return HttpResponse("Jan works!!")


# def feb(request):
#     return HttpResponse("Feb Works!!")

def monthly_challenges(request, month):
    if month == "january":
        challenge_text = "Jan Text!!"
    elif month == "february":
        challenge_text = "Feb Text!!"
    else :
        return HttpResponseNotFound("This month not supported!!")
    return HttpResponse(challenge_text)
