from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('members/', views.first, name='members_list'),
    path('members/athlete/', views.athlete, name='athlete'),
    path('members/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('signup/', views.signup, name='signup'),
]