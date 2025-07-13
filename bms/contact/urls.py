from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('suppliers/', SupplierListCreateView.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
     path('customers/<int:customer_id>/ledger/', CustomerLedgerView.as_view(), name='customer-ledger'),
    path('suppliers/<int:supplier_id>/ledger/', SupplierLedgerView.as_view(), name='supplier-ledger'),
]

