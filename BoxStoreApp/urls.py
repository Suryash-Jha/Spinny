from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('login/', views.loginx, name='login'),
    path('logout/', views.logoutx, name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.addBox, name='add'),
    path('update/<int:id>/', views.updateBox, name='update'),
    path('delete/<int:id>/', views.deleteBox, name='delete'),
    path('list/', views.listBox, name='list'),
    path('listMe/', views.listBoxMe, name='listMe'),
    path('constraints/', views.constraints_update, name='constraints'),
    
]
