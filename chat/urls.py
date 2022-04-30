from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<str:room>/', views.RoomView.as_view(), name='room'),
]
