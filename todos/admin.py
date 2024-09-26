from django.contrib.admin import ModelAdmin, register
from todos.models import Todo


@register(Todo)
class TodoAdmin(ModelAdmin):
    list_display = ["id", "title", "created"]
    search_fields = ["title", "description"]
    list_filter = ["created", "modified"]
    readonly_fields = ["id", "created", "modified"]
    fieldsets = (
        (None, {"fields": ("id", "title", "description")}),
        ("Metadata", {"fields": ("created", "modified")}),
    )
    ordering = ["id"]
