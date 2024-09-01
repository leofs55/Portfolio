from django.contrib import admin
from .models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone',)
    ordering = ('id',)
    search_fields = 'id', 'first_name', 'last_name'
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone'