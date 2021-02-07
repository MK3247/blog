from django.urls import path

from .views import Home, Detail

urlpatterns = [
    path('post/<int:pk>/', Detail.as_view(), name='detail'),
    path('', Home.as_view(), name = 'home'),
]
