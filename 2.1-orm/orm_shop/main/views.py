from django.http import Http404
from django.shortcuts import render

from .models import Car, Sale


def cars_list_view(request):
    # получите список авто

    q = request.GET.get('q', '')

    if q:
        cars = list(Car.objects.filter(model__icontains=q))
    else:
        cars = list(Car.objects.all())

    context = {
        'cars': cars
    }

    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404

    try:
        car = Car.objects.get(id=car_id)

        context = {
            'car': car
        }

        template_name = 'main/details.html'
        return render(request, template_name, context)  # передайте необходимый контекст

    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car = Car.objects.get(id=car_id)
        sales = list(Sale.objects.filter(car=car))

        context = {
            'car': car,
            'sales': sales
        }

        template_name = 'main/sales.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
