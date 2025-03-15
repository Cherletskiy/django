from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def get_dict():
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))

    bus_stations_list = get_dict()

    paginator = Paginator(bus_stations_list, 10)

    context = {
         'page': paginator.get_page(page_number),
    }
    return render(request, 'stations/index.html', context)

