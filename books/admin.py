from django.contrib import admin
from .models import Book, Genre
# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "published_date", "rating_average")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "author")
    list_filter = ("genre",)