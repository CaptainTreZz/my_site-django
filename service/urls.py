from django.urls import path
from service.views import index, page


urlpatterns = [
    path('service/', index),
    path('service/<int:page_num>', page)
]