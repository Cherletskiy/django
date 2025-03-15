import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_shop.settings")
django.setup()

from main.models import Car, Client, Sale
from django.utils.timezone import now
from faker import Faker
import random

fake = Faker("ru_RU")

# Данные автомобилей
cars_data = [
    {"model": "BMW X7", "year": 2023, "color": "Черный", "mileage": 5000, "volume": 3, "body_type": "SUV", "drive_unit": "full", "gearbox": "automatic", "fuel_type": "gasoline", "price": 12000000, "image": "images/bmw_x7.jpg"},
    {"model": "Geely Monjaro", "year": 2023, "color": "Синий", "mileage": 1000, "volume": 2, "body_type": "SUV", "drive_unit": "full", "gearbox": "automatic", "fuel_type": "gasoline", "price": 3500000, "image": "images/geely_monjaro.jpg"},
    {"model": "Mercedes G-Class", "year": 2023, "color": "Белый", "mileage": 3000, "volume": 4, "body_type": "SUV", "drive_unit": "full", "gearbox": "automatic", "fuel_type": "gasoline", "price": 20000000, "image": "images/gelandewagen.jpg"},
    {"model": "Hyundai Sonata", "year": 2022, "color": "Серый", "mileage": 15000, "volume": 2.5, "body_type": "sedan", "drive_unit": "front", "gearbox": "automatic", "fuel_type": "gasoline", "price": 2500000, "image": "images/hyundai_sonata.jpg"},
    {"model": "Lexus LX600", "year": 2023, "color": "Черный", "mileage": 5000, "volume": 3.5, "body_type": "SUV", "drive_unit": "full", "gearbox": "automatic", "fuel_type": "gasoline", "price": 15000000, "image": "images/lexus_lx600.jpg"},
    {"model": "Mercedes S-Class", "year": 2023, "color": "Серый", "mileage": 8000, "volume": 4, "body_type": "sedan", "drive_unit": "rear", "gearbox": "automatic", "fuel_type": "gasoline", "price": 18000000, "image": "images/mb_s_classe.jpg"},
    {"model": "Toyota Camry", "year": 2023, "color": "Белый", "mileage": 12000, "volume": 3.5, "body_type": "sedan", "drive_unit": "front", "gearbox": "automatic", "fuel_type": "gasoline", "price": 3200000, "image": "images/toyota_camry.jpg"},
    {"model": "Toyota Prius", "year": 2023, "color": "Зеленый", "mileage": 10000, "volume": 1.8, "body_type": "hatchback", "drive_unit": "front", "gearbox": "variator", "fuel_type": "hybrid", "price": 2700000, "image": "images/toyota_prius.jpeg"},
    {"model": "Lada Vesta SW Cross", "year": 2023, "color": "Оранжевый", "mileage": 5000, "volume": 1.6, "body_type": "wagon", "drive_unit": "front", "gearbox": "manual", "fuel_type": "gasoline", "price": 1800000, "image": "images/vesta_sw_cross.jpg"},
    {"model": "Volvo XC90", "year": 2023, "color": "Синий", "mileage": 8000, "volume": 3, "body_type": "SUV", "drive_unit": "full", "gearbox": "automatic", "fuel_type": "hybrid", "price": 9500000, "image": "images/volvo_xc90.jpg"},
]

# Добавление автомобилей в базу данных
for car_data in cars_data:
    Car.objects.create(**car_data)

print("Автомобили успешно добавлены в базу данных.")

# Создание 15 случайных клиентов
clients = []
for _ in range(15):
    client = Client.objects.create(
        name=fake.first_name(),
        last_name=fake.last_name(),
        middle_name=fake.middle_name(),
        date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=80),
        phone_number=fake.phone_number()
    )
    clients.append(client)

# Получаем все автомобили из базы данных
cars = list(Car.objects.all())

# Создание продаж для клиентов
for client in clients:
    if cars:
        car = random.choice(cars)
        Sale.objects.create(client=client, car=car, created_at=now())

print("Случайные клиенты и продажи успешно добавлены в базу данных.")
