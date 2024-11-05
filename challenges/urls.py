from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.jan),
    # path("february", views.feb),
    path("<int:month>", views.monthly_challenges_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge")
]
