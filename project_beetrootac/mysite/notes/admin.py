from django.contrib import admin
from .models import Note, Category

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'reminder')
    list_filter = ('category', 'reminder')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)

# Register your models here.