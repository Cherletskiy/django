from django.contrib import admin
from .models import *


# зарегистрируйте необходимые модели
admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Sale)
