from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('userpage/', views.userpage, name='userpage'),
    path('add_income/', views.addIncome, name="add_income"),
    path('add_expense/', views.addExpense, name="add_expense"),
    path('remove_income/', views.removeIncome, name="remove_income"),
    path('remove_expense/', views.removeExpense, name="remove_expense"),
]