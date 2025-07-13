from django.urls import path
from .views import *

urlpatterns = [
    path('expense-categories/', ExpenseCategory.as_view(), name='expense-categories'),
    path('income-categories/', IncomeCategory.as_view(), name='income-categories'),
    path('expenses/', ExpenseList.as_view(), name='expenses'),
    path('incomes/', IncomeList.as_view(), name='incomes'),
    path('reports/', FinanceReportView.as_view(), name='finance-reports'),
    path('expense_csv/', expense_csv, name='expense_csv'),
    path('expence_id_csv/', expense_id_csv, name = 'expense_id_csv'),
    path('income_csv/', income_csv, name='income_csv'),
    path('income_id_csv/',income_id_csv, name='income_id_csv'),
]