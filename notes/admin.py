from django.contrib import admin
from .models import Note, Tag, Category


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'owner', 'owner__username')


admin.site.register(Tag)
admin.site.register(Category)
