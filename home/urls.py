from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('delete/profile/<int:id>/', views.delete_profile, name="delete_profile"),
]
