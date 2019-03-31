from django.urls import path

from .views import citys, login

# url_tuple = [('login', login.login)]
# result = [path(x, y) for x, y in url_tuple]


# 应用命名空间
app_name = "api"
urlpatterns = [
    path('login', login.login, name="login"),
    path('user/me', login.get_user, name='user_me'),
    path('city', citys.CityView.as_view(), name="City"),
    path('city/calc', citys.CalcCity.as_view(), name="CalcCity"),
    path('user/<user_id>', login.get_url_params)
]
