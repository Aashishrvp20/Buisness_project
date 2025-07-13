from django.urls import path
from .views import *

urlpatterns = [
    path('suppliers/', SupplierListCreateView.as_view(), name='suppliers'),
    path('purchases/', PurchaseListCreateView.as_view(), name='purchases'),
    path('returns/', PurchaseReturnCreateView.as_view(), name='purchase-returns'),
    path('reports/', PurchaseReportsView.as_view(), name='purchase-reports'),
    path('purchase_csv/',purchase_csv,name='purchase_csv'),
    path('purchase_by_id_csv/<int:id>',purchase_id_csv,name='purchase_by__id_csv'),
    path('purchase_return_csv/<int:id>/',purchase_return_csv,name='purchase_return_csv'),
    
    path('supplier_csv/',supplier_csv,name='supplier_csv'),
    
    path('supplier_by_id_csv/<int:id>/',supplier_id_csv,name='supplier_by_id_csv'),
    
    
    
    
]
