from django.conf.urls import url
from . import views

app_name = 'fifth_app'


urlpatterns = [
    url('register', views.register,name='register'),
    url('user_login', views.user_login,name='user_login'),
]