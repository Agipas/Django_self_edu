from django.contrib import admin

from .models import Post


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created', 'date_updated', 'author', 'category')
    list_display_link = ('id', 'title')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PageAdmin)
