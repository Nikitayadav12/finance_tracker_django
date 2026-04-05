from finance.models import FinanceEntry
from django.db.models import Sum

def calculate_financial_summary(user):
    income = FinanceEntry.objects.filter(user=user, type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = FinanceEntry.objects.filter(user=user, type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    balance = income - expense
    status = "Profit" if balance > 0 else "Loss"

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": balance,
        "status": status
    }


def category_breakdown(user):
    return FinanceEntry.objects.filter(user=user)\
        .values('category')\
        .annotate(total=Sum('amount'))