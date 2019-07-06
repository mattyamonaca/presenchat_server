from django.urls import path

from . import main, views

urlpatterns = [
    path('message/', main.do_main, name='do_main'),
]
