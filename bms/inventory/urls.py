from django.urls import path
from .views import *
urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('stock-entry/', StockEntryCreateView.as_view(), name='stock-entry'),
    path('product_csv/', product_csv,name='product_csv'),
    path('product_id_csv/<int:id>/', product_id_csv,name='product_id_csv'),
]