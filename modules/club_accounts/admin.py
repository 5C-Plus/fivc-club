from django.contrib import admin

from .models import (
    Account,
    TransactionCategory,
    Transaction,
)


class AccountAdmin(admin.ModelAdmin):
    """
    club dependency admin
    """

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'club', 'created_by', 'modified_by')


class TransactionCategoryAdmin(admin.ModelAdmin):
    """
    transaction category admin
    """

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'created_by', 'modified_by')


class TransactionAdmin(admin.ModelAdmin):
    """
    transaction admin
    """

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'category',
            'account',
            'account__club',
            'created_by',
            'modified_by',
        )


admin.site.register(Account, AccountAdmin)
admin.site.register(TransactionCategory, TransactionCategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)
