from django.contrib import admin

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'date_added']
    list_display = ['name', 'id', 'date_added']

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
