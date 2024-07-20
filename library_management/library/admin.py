from django.contrib import admin
from .models import Author, Book, BorrowRecord


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'published_date', 'author')
    search_fields = ('title', 'genre')


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'book', 'borrow_date', 'return_date')
    search_fields = ('user_name', 'book')
