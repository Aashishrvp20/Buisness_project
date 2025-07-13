from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,UpdateAPIView
from .models import *
from .serializers import *
from users.permissions import Manager
from rest_framework.response import Response
from rest_framework import status
from quotation.models import Quotations
from users.permissions import Manager,Staff
from sales.models import *
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend

class Quotationcreateview(ListCreateAPIView):
    permission_classes=[Staff]
    serializer_class=QuotationsSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=QuotationFilter
    

class QuotationSetview(RetrieveUpdateDestroyAPIView):
    permission_classes=[Manager]
    serializer_class=QuotationsSerializer

class ConvertQuotationToSaleView(UpdateAPIView):
    permission_classes = [Manager]
    queryset = Quotations.objects.all()

    def update(self, request, *args, **kwargs):
        quotation = self.get_object()

        # dont let the conversion happen multiple times
        if quotation.approved:
            return Response({"error": "Quotation already approved."}, status=status.HTTP_400_BAD_REQUEST)

        # make sure that quotation has a valid product 
        if not quotation.product:
            return Response({"error": "Quotation has no product."}, status=status.HTTP_400_BAD_REQUEST)

        product = quotation.product
        customer = quotation.customer
        if not customer:
            return Response({"error": "Quotation has no associated customer."}, status=status.HTTP_400_BAD_REQUEST)

        sale = Sale.objects.create(
            customer=customer,
            total=quotation.amount,
            discount=quotation.discount,
            tax=0,
            paid=0,
            is_paid=False,
            created_by=request.user
        )

        SaleItem.objects.create(
            sale=sale,
            product=product,
            quantity=quotation.quantity,
            price=quotation.rate
        )

        # since  all the thing match toggle the approved.
        quotation.approved = True
        quotation.save()

        return Response({"message": "Quotation successfully converted to sale."}, status=status.HTTP_200_OK)
