import json
from .models import *
from django.db.models import Sum


def userData(request):
    if request.user.is_authenticated:
        person = request.user.person
        person_incomes = Income.objects.filter(person=person).values()
    
        person = request.user.person
        person_expenses = Expense.objects.filter(person=person).values()
    
    return {'incomes': person_incomes, 'expenses': person_expenses, 'user': person}

def getTotals(request):
    person = request.user.person
    
    incomes_total = Income.objects.filter(person=person).values_list('amount', flat=True)
    total_incomes = sum([total for total in incomes_total])
    
    expenses_total = Expense.objects.filter(person=person).values_list('amount', flat=True)
    total_expenses = sum([total for total in expenses_total])
    
    return {'total_incomes': total_incomes, 'total_expenses': total_expenses}