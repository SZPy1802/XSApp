from django.contrib import admin
from django.urls import path
from artapp import views

app_name = 'artapp'
urlpatterns = [
    # 声明主页面的请求
    path('', views.index),
]
