from django.urls import path
from . import views

urlpatterns = [
    path('predict_temperature/', views.predict_temperature, name='predict_temperature'),
]
