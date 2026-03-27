from django.contrib import admin
from .models import Recommendation

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "created_at")
    search_fields = ("user__username", "book__title", "comment")
    list_filter = ("created_at",)