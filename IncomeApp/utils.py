import json
from .models import *
from django.db.models import Sum


def userData(request):
    if request.user.is_authenticated:
        person = request.user.person
        person_incomes = Income.objects.filter(person=person).values()
        person_expenses = Expense.objects.filter(person=person).values()
    else:
        return {}
    
    return {'incomes': person_incomes, 'expenses': person_expenses, 'user': person}


def getTotals(request):
    person = request.user.person
    
    incomes_total = Income.objects.filter(person=person).values_list('amount', flat=True)
    total_incomes = sum([total for total in incomes_total])
    
    expenses_total = Expense.objects.filter(person=person).values_list('amount', flat=True)
    total_expenses = sum([total for total in expenses_total])
    
    final_total = total_incomes - total_expenses
        
    if final_total >= 0:
        final_total = "+£" + str(final_total)
    else:
        final_total = "-£" + str(abs(final_total))
    
    return {'total_incomes': total_incomes, 'total_expenses': total_expenses, 'final_total': final_total}

def incomesLimit(request):
    person = request.user.person
    
    incomes_count = len([i for i in Income.objects.filter(person=person)])
    print(incomes_count)
    
    return {'incomes_count': incomes_count}

def expensesLimit(request):
    person = request.user.person
    
    expenses_count = len([i for i in Expense.objects.filter(person=person)])
    print(expenses_count)
    
    return {'expenses_count': expenses_count}