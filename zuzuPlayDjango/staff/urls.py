from django.urls import path
from .views import administration

urlpatterns = [
    path('administration/', administration, name="administration"),
]