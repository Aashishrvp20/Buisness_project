# permissions.py
from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    allowed_roles = []

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in self.allowed_roles

class Admin(RolePermission):
    allowed_roles = ['admin']

class Manager(RolePermission):
    allowed_roles = ['admin', 'manager']

class Staff(RolePermission):
    allowed_roles = ['admin', 'staff','manager']

class Customer(RolePermission):
    allowed_roles = ['customer','admin']

class Instructor(RolePermission):
    allowed_roles = ['instructor','admin','manager']

class Student(RolePermission):
    allowed_roles = ['student','admin','staff']
