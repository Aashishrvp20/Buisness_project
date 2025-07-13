from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,CreateAPIView,GenericAPIView
from .models import *
from contact.models import Customer
from .serializers import *
import tablib
from django.http import HttpResponse
from rest_framework.response import Response
from django.utils.timezone import timedelta,now
from django.db.models import Sum
from users.permissions import Manager,Staff
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *

class SaleListCreateView(ListCreateAPIView):
    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SaleFilter
    permission_classes = [Staff]  
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [Staff]


class SaleReturnCreateView(CreateAPIView):
    queryset = SaleReturn.objects.all()
    serializer_class = SaleReturnSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SaleReturnFilter
    permission_classes = [Staff]

class SalesAnalyticsView(GenericAPIView):
    permission_classes = [Manager]

    def get(self, request, *args, **kwargs):
        today = now().date()
        last_7_days = today - timedelta(days=7)
        last_30_days = today - timedelta(days=30)

        sales_7 = Sale.objects.filter(date__date__gte=last_7_days).aggregate(total_sales=Sum('total'))['total_sales'] or 0
        sales_30 = Sale.objects.filter(date__date__gte=last_30_days).aggregate(total_sales=Sum('total'))['total_sales'] or 0

        returns_7 = SaleReturn.objects.filter(date__date__gte=last_7_days).aggregate(total_refund=Sum('refund_amount'))['total_refund'] or 0
        returns_30 = SaleReturn.objects.filter(date__date__gte=last_30_days).aggregate(total_refund=Sum('refund_amount'))['total_refund'] or 0

        data = {
            "sales_7days": sales_7,
            "sales_30days": sales_30,
            "returns_7days": returns_7,
            "returns_30days": returns_30,
            "total_last_7days": sales_7 - returns_7,
            "total_last_30days": sales_30 - returns_30,
        }

        serializer = SalesAnalyticsSerializer(data)
        return Response(serializer.data)
    

"""here is list of views to print excel files----------------------------"""

def customer_csv(request): # Customer
    # Prepare your dataset
        dataset = tablib.Dataset()
        dataset.headers = ['name', 'phone', 'email', 'address ','notes','opening_blnc',"pan_no","date_created"]
    
    # Add your data
        for obj in Customer.objects.all():
            dataset.append([obj.name, obj.phone, obj.email, obj.address,obj.notes,obj.opening_blnc,obj.pan_no,obj.date_created])
    
    # Create response with CSV data
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        return response


def customerid_csv(request,id): # customer-id
    # Prepare your dataset
        dataset = tablib.Dataset()
        dataset.headers = ['name', 'phone', 'email', 'address ','notes','opening_blnc',"pan_no","date_created"]
    
    # Add your data
        for obj in Customer.objects.filter(id=id):
            dataset.append([obj.name, obj.phone, obj.email, obj.address,obj.notes,obj.opening_blnc,obj.pan_no,obj.date_created])
    
    # Create response with CSV data
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        return response


def sales_csv(request): # sale
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['customer', 'date', 'total', 'discount','tax','paid',"is_paid","created_by"]
    
    # Add your data
    for obj in Sale.objects.all():
        dataset.append([obj.customer, obj.date, obj.total, obj.discount,obj.tax,obj.paid,obj.is_paid,obj.created_by])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    return response


def salesid_csv(request,id): # sale by id
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['customer', 'date', 'total', 'discount','tax','paid',"is_paid","created_by"]
    

    # Add your data
    for obj in Sale.objects.filter(id=id):
        dataset.append([obj.customer, obj.date, obj.total, obj.discount,obj.tax,obj.paid,obj.is_paid,obj.created_by])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    return response


def salesreturn_csv(request): # salereturn
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['sale', 'date', 'refund_amount']
    
    # Add your data
    for obj in SaleReturn.objects.all():
        dataset.append([obj.sale, obj.date, obj.refund_amount])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    return response
def salesreturnid_csv(request,id): # salereturn
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['sale', 'date', 'refund_amount']
    
    # Add your data
    for obj in SaleReturn.objects.filter(id=id):
        dataset.append([obj.sale, obj.date, obj.refund_amount])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    return response

