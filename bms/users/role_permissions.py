from django.contrib.auth.models import Permission

def get_role_permissions():
    return {
        'admin': Permission.objects.all(),
        'manager': Permission.objects.filter(codename__in=[
            'add_customer', 'change_customer', 'view_customer',

            'add_course', 'change_course', 'view_course',
            'add_enrollment', 'change_enrollment', 'view_enrollment',
            'add_instructor', 'change_instructor', 'view_instructor',
            'add_student', 'change_student', 'view_student',

            'add_expense', 'change_expense', 'view_expense',
            'add_expensecategory', 'change_expensecategory', 'view_expensecategory',
            'add_income', 'change_income', 'view_income',
            'add_incomecategory', 'change_incomecategory', 'view_incomecategory',

            'add_category', 'change_category', 'view_category',
            'add_product', 'change_product', 'view_product',
            'add_stockentry', 'change_stockentry', 'view_stockentry',

            'add_purchase', 'change_purchase', 'view_purchase',
            'add_purchaseitem', 'change_purchaseitem', 'view_purchaseitem',
            'add_supplier', 'change_supplier', 'view_supplier',

            'add_quotations', 'change_quotations', 'view_quotations',

            'add_sale', 'change_sale', 'view_sale',
            'add_saleitem', 'change_saleitem', 'view_saleitem',

            'add_user', 'change_user', 'view_user',
        ]),
        'staff': Permission.objects.filter(codename__in=[
            'view_customer', 'view_course', 'view_enrollment', 'view_instructor', 'view_student',
            'view_expense', 'view_expensecategory', 'view_income', 'view_incomecategory',
            'view_category', 'view_product', 'view_stockentry',
            'view_purchase', 'view_purchaseitem', 'view_supplier',
            'view_quotations',
            'view_sale', 'view_saleitem',
            'view_user',
        ]),
    }
