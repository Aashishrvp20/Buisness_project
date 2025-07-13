from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.db.models import Sum
from django.utils.timezone import now, timedelta
from sales.models import Sale
from purchase.models import Purchase
from finance.models import Expense, Income
from inventory.models import Product
from users.permissions import Manager

class DashboardReportView(GenericAPIView):
    permission_classes = [Manager]

    def get(self, request):
        today = now().date()
        last_7_days = today - timedelta(days=7)
        last_30_days = today - timedelta(days=30)

        # all the sales data are here 
        sales_7 = Sale.objects.filter(date__gte=last_7_days).aggregate(total=Sum('total'))['total'] or 0
        sales_30 = Sale.objects.filter(date__gte=last_30_days).aggregate(total=Sum('total'))['total'] or 0

        # all the purchases data are here
        purchases_7 = Purchase.objects.filter(date__gte=last_7_days).aggregate(total=Sum('total'))['total'] or 0
        purchases_30 = Purchase.objects.filter(date__gte=last_30_days).aggregate(total=Sum('total'))['total'] or 0

        # all the Expenses & Income data are here
        expenses_7 = Expense.objects.filter(date__gte=last_7_days).aggregate(total=Sum('amount'))['total'] or 0
        incomes_7 = Income.objects.filter(date__gte=last_7_days).aggregate(total=Sum('amount'))['total'] or 0

        # all low stock are showwn here 
        low_stock_products = Product.objects.filter(stock__lte=10).count()

        data = {
            "sales_7days": sales_7,
            "sales_30days": sales_30,
            "purchaseslast_7days": purchases_7,
            "purchaseslast_30days": purchases_30,
            "expenseslast_7days": expenses_7,
            "incomeslast_7days": incomes_7,
            "netincomelast_7days": incomes_7 - expenses_7,
            "lowstockproducts_count": low_stock_products,
        }
        return Response(data)

