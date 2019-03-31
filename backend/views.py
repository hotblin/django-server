from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.


def create_user(request):
    user = User.objects.create_user()
