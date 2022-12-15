from django.urls import path
from .import views

app_name = "base"

urlpatterns = [
    path("", views.homePage, name='home'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('insurance/', views.insurance, name='insurance'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('user-profile/<str:pk>/', views.userProfile, name='profile'),
    path('update-user/', views.updateUser, name='profile-update'),
    path('change-password/', views.changePassword, name='change-password'),
    path('checkout/', views.checkout, name='checkout'),
    
]