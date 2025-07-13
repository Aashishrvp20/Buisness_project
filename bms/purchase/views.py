from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,CreateAPIView,GenericAPIView
from .models import Supplier,Purchase,PurchaseItem,PurchaseReturn,PurchaseReturnItem
from .serializers import *
from users.permissions import Manager,Staff
from rest_framework.response import Response
from django.db.models import Sum
import tablib
from django.http import HttpResponse
from contact.serializers import SupplierSerializer
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend   

from django.utils.timezone import now, timedelta


class SupplierListCreateView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    permission_classes = [Staff]

class PurchaseListCreateView(ListCreateAPIView):
    queryset = Purchase.objects.all().order_by('-date')
    serializer_class = PurchaseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaseFilter
    permission_classes = [Staff]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PurchaseReturnCreateView(ListCreateAPIView):
    queryset = PurchaseReturn.objects.all()
    serializer_class = PurchaseReturnSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaseReturnFilter
    permission_classes = [Staff]

class PurchaseReportsView(GenericAPIView):
    permission_classes = [Manager]

    def get(self, request):
        today = now().date()
        last_7_days = today - timedelta(days=7)
        last_30_days = today - timedelta(days=30)

        purchases_7 = Purchase.objects.filter(date__date__gte=last_7_days).aggregate(total=Sum('total'))['total'] or 0
        purchases_30 = Purchase.objects.filter(date__date__gte=last_30_days).aggregate(total=Sum('total'))['total'] or 0

        returns_7 = PurchaseReturn.objects.filter(date__date__gte=last_7_days).aggregate(total_refund=Sum('refund_amount'))['total_refund'] or 0
        returns_30 = PurchaseReturn.objects.filter(date__date__gte=last_30_days).aggregate(total_refund=Sum('refund_amount'))['total_refund'] or 0

        data = {
            "purchases_7days": purchases_7,
            "purchases_30days": purchases_30,
            "returns_7days": returns_7,
            "returns_30days": returns_30,
            "total_7days": purchases_7 - returns_7,
            "total_30days": purchases_30 - returns_30,
        }

        return Response(data)
    
def purchase_csv(request): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['supplier','date','User', 'total', 'paid', 'is_paid']
    
    # Add your data
    for obj in Purchase.objects.all():
        dataset.append([obj.supplier,obj.date ,obj.created_by,obj.total, obj.paid, obj.is_paid])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="purchase.csv"'
    return response


def purchase_id_csv(request,id): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['supplier','date','User', 'total', 'paid', 'is_paid']
    
    # Add your data
    for obj in Purchase.objects.filter(id=id):
        dataset.append([obj.supplier,obj.date ,obj.created_by,obj.total, obj.paid, obj.is_paid])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="purchase_by_id.csv"'
    return response


def supplier_csv(request): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['name','date' ,'User','phone', 'email', 'address']
    
    # Add your data
    for obj in Supplier.objects.all():
        dataset.append([obj.name,obj.date,obj.created_by ,obj.phone, obj.email, obj.address])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="supplier.csv"'
    return response

def supplier_id_csv(request,id): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['name','date' ,'phone', 'email', 'address']
    
    # Add your data
    for obj in Supplier.objects.filter(id=id):
        dataset.append([obj.name,obj.date ,obj.phone, obj.email, obj.address])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="supplier_by_id.csv"'
    return response

def purchase_return_csv(request,id): # customer
    # Prepare your dataset
    dataset = tablib.Dataset()
    dataset.headers = ['purchase', 'refund_amount', 'date']
    
    # Add your data
    for obj in PurchaseReturn.objects.filter(id=id):
        dataset.append([obj.supplier, obj.total, obj.paid, obj.is_paid])
    
    # Create response with CSV data
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="purchase_return.csv"'
    return response