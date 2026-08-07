from django.contrib import admin
from .models import FeedbackEntry

@admin.register(FeedbackEntry)
class FeedbackEntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'topic', 'rating', 'created_at']
    list_filter = ['topic', 'rating']
