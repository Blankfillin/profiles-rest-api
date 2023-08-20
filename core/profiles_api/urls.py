from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
