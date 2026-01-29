from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('', views.first, name='members_list'),  # Root path shows members list
    path('members/', views.athlete, name='athlete'),
    path('members/list/', views.first, name='members_list_alt'),  # Alternative path for members list
    path('members/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]