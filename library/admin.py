from django.contrib import admin
from .models import Book, Comment
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_book', 'owner', 'show',)
    ordering = ('id',)
    search_fields = ('id', 'title', 'owner',)
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('title', 'owner', 'show',)
    list_display_links = ('id',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'show',)
    ordering = ('id',)
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('post', 'author', 'show',)
    list_display_links = ('id',)
