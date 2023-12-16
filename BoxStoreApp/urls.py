from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('login/', views.loginx, name='login'),
    path('logout/', views.logoutx, name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.addBox, name='add'),
    path('update/<int:id>/', views.updateBox, name='update'),
    path('delete/<int:id>/', views.deleteBox, name='delete'),
]
