from django.urls import path
from .views import *

urlpatterns = [
    path('sales/', SaleListCreateView.as_view(), name='sales'),
    path('customers/', CustomerListCreateView.as_view(), name='customers'),
    path('returns/', SaleReturnCreateView.as_view(), name='sale-returns'),
    path('analytics/', SalesAnalyticsView.as_view(), name='sales-analytics'),
    path('customercsv/', customer_csv, name='show'),
    path('customercsv/<int:id>/', customerid_csv, name='show'),
    path('salescsv/', sales_csv, name='show'),
    path('salescsv/<int:id>/', salesid_csv, name='show'),
    path('salesreturncsv/', salesreturn_csv, name='show'),
    path('salesreturncsv/<int:id>/', salesreturnid_csv, name='show'),


]
