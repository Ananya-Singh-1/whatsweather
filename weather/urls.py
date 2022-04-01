from django.urls import URLPattern, path, include
from weather import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('weather/', views.DescriptionViewSet)

URLPatterns = [
    path('',include(router.urls))
]