from django.urls import path
from .api import StudentApi
urlpatterns = [
    path('',StudentApi.as_view()),
]