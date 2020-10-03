from django.urls import path

from csvApp import views


urlpatterns = [
    path('', views.ServeReactApp.as_view(), name='homepage'),
]
