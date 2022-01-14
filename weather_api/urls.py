from django.urls import path, include
from weather_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('description/', views.DescriptionViewset)

urlpatterns = [
    path('', include(router.urls))
]