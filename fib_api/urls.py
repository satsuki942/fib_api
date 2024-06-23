from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FibNView

urlpatterns = [
    path('', FibNView.as_view(),name='fib'),
    path('/', FibNView.as_view(),name='fib_slash'),
]
