from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
import json

from .models import *
from .utils import userData, getTotals, incomesLimit, expensesLimit

# Create your views here.
def home(request):
    context = {}
    return render(request, 'incomeapp/home.html', context)

def login(request):
    if request.method == "POST":
        if "login-button" in request.POST:
            username = request.POST['username-input']
            password = request.POST['password-input']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('userpage')
            else:
                messages.success(request, ("No user found. Please try again or create a new user with that Username."))
                return redirect('login')
        elif "newuser-button" in request.POST:
            username = request.POST['username-input']
            password = request.POST['password-input']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, ("User already exists. Please try again or create a new user with a different Username."))
                return redirect('login')
            else:
                new_user = User.objects.create_user(username=username, password=password)
                Person.objects.create(user=new_user, name=username)
                
                messages.success(request, ("User created. You may log in."))
                return redirect('login')
    else:
        context = {}
        return render(request, 'incomeapp/login.html', context)
    
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    
    return JsonResponse("Logged out", safe=False)

def userpage(request):
    data = userData(request)
    context = {}
    if data:
        incomes = data['incomes']
        expenses = data['expenses']
        user = data['user']
        totals_data = getTotals(request)
        total_incomes = totals_data['total_incomes']
        total_expenses = totals_data['total_expenses']
        final_total = totals_data['final_total']
            
        context = {'incomes': incomes, 'expenses': expenses, 'total_incomes': total_incomes, 'total_expenses': total_expenses, 'final_total': final_total, 'user': user}
        
    return render(request, 'incomeapp/userpage.html', context)

def addIncome(request):
    data = json.loads(request.body)
    income_amount = data['income_amount']
    income_name = data['income_name']
    
    if len(income_name) > 12 or len(income_amount) > 5:
        return JsonResponse("Name too long.", safe=False)
    
    if incomesLimit(request)['incomes_count'] > 16:
        return JsonResponse("Limit reached.", safe=False)
    
    person = request.user.person
    Income.objects.get_or_create(person=person, name=income_name, amount=income_amount)
    
    return JsonResponse("Income added.", safe=False)

def addExpense(request):
    data = json.loads(request.body)
    expense_amount = data['expense_amount']
    expense_name = data['expense_name']
    
    if len(expense_name) > 12 or len(expense_amount) > 5:
        return JsonResponse("Name too long.", safe=False)
    
    if expensesLimit(request)['expenses_count'] > 16:
        return JsonResponse("Limit reached.", safe=False)
    
    person = request.user.person
    Expense.objects.get_or_create(person=person, name=expense_name, amount=expense_amount)
    
    return JsonResponse("Expense added.", safe=False)

def removeIncome(request):
    data = json.loads(request.body)
    income_name = data['income_name']
    
    person = request.user.person
    
    Income.objects.filter(person=person, name=income_name).delete()
    
    return JsonResponse("Income removed.", safe=False)

def removeExpense(request):
    data = json.loads(request.body)
    expense_name = data['expense_name']
    
    person = request.user.person
    
    Expense.objects.filter(person=person, name=expense_name).delete()
    
    return JsonResponse("Expense removed.", safe=False)
