from django.contrib import admin
from .models import Adventure, Destination_comment
# Register your models here.

admin.site.register(Adventure)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user', 'content')


admin.site.register(Destination_comment, CommentAdmin)
