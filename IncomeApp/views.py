from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *
from .utils import userData, getTotals

# Create your views here.
def home(request):
    context = {}
    return render(request, 'incomeapp/home.html', context)

def login(request):
    context = {}
    return render(request, 'incomeapp/login.html', context)

def loginUser(request):
    data = userData(request)
    username = data['username']
    email = data['email']
    
    person = request.user.person
    new_user = Person.objects.get_or_create(user=person, name=username, email=email)
    
    new_user.save()
    
    return JsonResponse("yes", safe=False)

def userpage(request):
    data = userData(request)
    incomes = data['incomes']
    expenses = data['expenses']
    user = data['user']
    totals_data = getTotals(request)
    total_incomes = totals_data['total_incomes']
    total_expenses = totals_data['total_expenses']
    
    final_total = total_incomes - total_expenses
    
    if final_total >= 0:
        final_total = "+£" + str(final_total)
    else:
        final_total = "-£" + str(abs(final_total))
        
    context = {'incomes': incomes, 'expenses': expenses, 'total_incomes': total_incomes, 'total_expenses': total_expenses, 'final_total': final_total, 'user': user}
    return render(request, 'incomeapp/userpage.html', context)

def addIncome(request):
    data = json.loads(request.body)
    income_amount = data['income_amount']
    income_name = data['income_name']
    
    person = request.user.person
    new_income = Income.objects.get_or_create(person=person, name=income_name, amount=income_amount)
    
    new_income.save()
    
    return JsonResponse("yes", safe=False)

def addExpense(request):
    data = json.loads(request.body)
    expense_amount = data['expense_amount']
    expense_name = data['expense_name']
    
    person = request.user.person
    new_expense = Expense.objects.get_or_create(person=person, name=expense_name, amount=expense_amount)
    
    new_expense.save()
    
    return JsonResponse("yes", safe=False)

def removeIncome(request):
    data = json.loads(request.body)
    income_name = data['income_name']
    
    person = request.user.person
    
    Income.objects.filter(person=person, name=income_name).delete()
    
    return JsonResponse("yes", safe=False)

def removeExpense(request):
    data = json.loads(request.body)
    expense_name = data['expense_name']
    
    person = request.user.person
    
    Expense.objects.filter(person=person, name=expense_name).delete()
    
    return JsonResponse("yes", safe=False)
