from django.contrib import admin
from .models import Contact, Category


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone',
        'email',
        'created_date',
        'show',
    ]
    ordering = ['-id']
    list_editable = [
        'show',
    ]
    list_per_page = 15


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
