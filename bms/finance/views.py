from rest_framework.generics import ListCreateAPIView,GenericAPIView
from .models import *
from .serializers import  *
from users.permissions import Manager,Staff
from rest_framework.response import Response
from django.db.models import Sum
from django.utils.timezone import now, timedelta
import tablib
from django.http import HttpResponse
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend


# expenses for today

class ExpenseCategory(ListCreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_classes = [Staff]

class IncomeCategory(ListCreateAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
    permission_classes = [Staff]

class ExpenseList(ListCreateAPIView):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenseFilter
    permission_classes = [Manager]

class IncomeList(ListCreateAPIView):
    queryset = Income.objects.all().order_by('-date')
    serializer_class = IncomeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IncomeFilter
    permission_classes = [Manager]



class FinanceReportView(GenericAPIView):
    permission_classes = [Manager]

    def get(self, request):
        today = now().date()
        last_7_days = today - timedelta(days=7)
        last_30_days = today - timedelta(days=30)

        expenses_7 = Expense.objects.filter(date__gte=last_7_days).aggregate(total=Sum('amount'))['total'] or 0
        expenses_30 = Expense.objects.filter(date__gte=last_30_days).aggregate(total=Sum('amount'))['total'] or 0

        incomes_7 = Income.objects.filter(date__gte=last_7_days).aggregate(total=Sum('amount'))['total'] or 0
        incomes_30 = Income.objects.filter(date__gte=last_30_days).aggregate(total=Sum('amount'))['total'] or 0

        return Response({
            "expenses_last_7_days": expenses_7,
            "expenses_last_30_days": expenses_30,
            "incomes_last_7_days": incomes_7,
            "incomes_last_30_days": incomes_30,
            "net_last_7_days": incomes_7 - expenses_7,
            "net_last_30_days": incomes_30 - expenses_30,
        })

def expense_csv(request): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = [ 'category', 'amount', 'date','description','receipt']
    
    # Add your data
    for obj in Expense.objects.all():
        dataset.append([obj.category, obj.amount, obj.date, obj.description,obj.receipt])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expense.csv"'
    return response

def expense_id_csv(request,id): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = [ 'category', 'amount', 'date','description','receipt']
    
    # Add your data
    for obj in Expense.objects.filter(id=id):
        dataset.append([obj.category, obj.amount, obj.date, obj.description,obj.receipt])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expense_by_id.csv"'
    return response

def income_id_csv(request,id): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = [ 'category', 'amount', 'date','description','receipt']
    
    # Add your data
    for obj in Income.objects.filter(id=id):
        dataset.append([obj.category, obj.amount, obj.date, obj.description,obj.receipt])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="income_by_id.csv"'
    return response


def income_csv(request): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = [ 'category', 'amount', 'date','description','receipt']
    
    # Add your data
    for obj in Expense.objects.all():
        dataset.append([obj.category, obj.amount, obj.date, obj.description,obj.receipt])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="income.csv"'
    return response