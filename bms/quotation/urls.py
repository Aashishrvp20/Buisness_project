from django.urls import path
from .views import Quotationcreateview,QuotationSetview,ConvertQuotationToSaleView

urlpatterns = [
    path('quotation/',Quotationcreateview.as_view(), name='quotation-list-create'),
    path('quotation/<int:pk>/', QuotationSetview.as_view(), name='quotation-detail'),
    path('convert-to-sale/<int:pk>/', ConvertQuotationToSaleView.as_view(), name='convert-to-sale'),
]
