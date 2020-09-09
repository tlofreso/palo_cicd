from django.urls import path
from . import views

urlpatterns = [path("", views.firewall, name="firewall-firewall")]

