from django_filters.rest_framework import DjangoFilterBackend
from .filters import CustomerFilter
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView
from .models import Customer
from purchase.models import Supplier
from sales.models import Sale, SaleReturn
from django.db.models import Sum
from purchase.models import Purchase, PurchaseReturn
from .serializers import *
from users.permissions import Manager,Staff,Admin
from rest_framework.response import Response
import tablib
from django.http import HttpResponse

class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [Staff]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomerFilter

class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [Manager]

class SupplierListCreateView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [Staff]

class SupplierDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [Manager]

class CustomerLedgerView(GenericAPIView):
    permission_classes = [Admin]

    def get(self, request, customer_id):
        total_sales = Sale.objects.filter(customer_id=customer_id).aggregate(total=Sum('total'))['total'] or 0
        total_paid = Sale.objects.filter(customer_id=customer_id).aggregate(paid=Sum('paid'))['paid'] or 0
        total_returns = SaleReturn.objects.filter(sale__customer_id=customer_id).aggregate(refund=Sum('refund_amount'))['refund'] or 0

        balance_due = total_sales - total_paid - total_returns

        data = {
            "customer_id": customer_id,
            "total_sales": total_sales,
            "total_paid": total_paid,
            "total_returns": total_returns,
            "balance_due": balance_due
        }

        serializer = CustomerLedgerSerializer(data)
        return Response(serializer.data)


class SupplierLedgerView(GenericAPIView):
    permission_classes = [Admin]

    def get(self, request, supplier_id):
        total_purchases = Purchase.objects.filter(supplier_id=supplier_id).aggregate(total=Sum('total'))['total'] or 0
        total_paid = Purchase.objects.filter(supplier_id=supplier_id).aggregate(paid=Sum('paid'))['paid'] or 0
        total_returns = PurchaseReturn.objects.filter(purchase__supplier_id=supplier_id).aggregate(refund=Sum('refund_amount'))['refund'] or 0

        balance_due = total_purchases - total_paid - total_returns

        data = {
            "supplier_id": supplier_id,
            "total_purchases": total_purchases,
            "total_paid": total_paid,
            "total_returns": total_returns,
            "balance_due": balance_due
        }

        serializer = SupplierLedgerSerializer(data)
        return Response(serializer.data)
    
   
    

    def Supplier_csv(request): # Suppliers
    # Prepare your dataset
        dataset = tablib.Dataset()
        dataset.headers = ['name', 'phone', 'email', 'address ','notes','opening_blnc',"pan_no","date_created"]
    
    # Add your data
        for obj in Supplier.objects.all():
            dataset.append([obj.name, obj.phone, obj.email, obj.address,obj.notes,obj.opening_blnc,obj.pan_no,obj.date_created])
    
    # Create response with CSV data
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        return response 
    
    
    def Supplier_id_csv(request,id): # customer-id
    # Prepare your dataset
        dataset = tablib.Dataset()
        dataset.headers = ['name', 'phone', 'email', 'address ','notes','opening_blnc',"pan_no","date_created"]
    
    # Add your data
        for obj in Supplier.objects.filter(id=id):
            dataset.append([obj.name, obj.phone, obj.email, obj.address,obj.notes,obj.opening_blnc,obj.pan_no,obj.date_created])
    
    # Create response with CSV data
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        return response  