from django.contrib import admin

from accounts.models import Role, UserRole
from main.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    pass
