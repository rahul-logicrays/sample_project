from django.http import HttpResponse

from .models import Date

# from django.shortcuts import render


# Create your views here.
def date(request):
    date = "2022-10-05"
    new = Date(date=date)
    new.save()
    return HttpResponse("success")
