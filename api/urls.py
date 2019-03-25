from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sub_index', views.sub_index, name="sub_index")
]
