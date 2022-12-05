from django.urls import path
from rest_framework import routers

# from .views.core import

ROUTER = routers.DefaultRouter()

# ROUTER.register('contact_request', ContactViewSet, basename='contact-viewset')

urlpatterns = ROUTER.urls
