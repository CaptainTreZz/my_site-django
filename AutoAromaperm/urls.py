from django.contrib import admin
from django.urls import path
from service.views import index

urlpatterns = [
    path('service/', index),
    path('admin/', admin.site.urls),
]
