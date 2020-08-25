from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<int:pk>/',views.update, name='update'),
    path('<int:pk>/delete/',views.delete, name='delete'),
    path('weather/',views.weather, name='weather'),
    path('photo/',views.photo, name='photo'),
    # path('detail/<int:pk>/',views.detail, name='Read'),
]