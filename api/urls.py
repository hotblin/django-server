from django.urls import path

from .views import citys, login

# url_tuple = [('login', login.login)]
# result = [path(x, y) for x, y in url_tuple]

urlpatterns = [
    path('login', login.login, name="login"),
    path('user/me', login.get_user, name='user_me'),
    path('city', citys.CityView.as_view(), name="City"),
    path('city/calc', citys.CalcCity.as_view(), name="CalcCity")
]
