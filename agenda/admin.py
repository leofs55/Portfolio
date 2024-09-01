from django.contrib import admin
from .models import Contact, Category

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show',)
    ordering = ('id',)
    search_fields = 'id', 'first_name', 'last_name'
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name', 'show',
    list_display_links = 'id', 'phone'


@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('id',)
