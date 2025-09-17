from django.contrib import admin, messages
from .models import *
# Register your models here.

@admin.action(description='active status ...')
def active_status(modeladmin, request, queryset):
    updated = queryset.update(status=True)
    messages.success(request, f'{updated} status ...')
    
@admin.action(description='deactive status ...')
def deactive_status(modeladmin, request, queryset):
    updated = queryset.update(status=False)
    messages.success(request, f'{updated} status ...')
    

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'status', 'created_at')
    list_filter = ('status','created_at')
    search_fields = ('title', 'slug')
    actions = [active_status, deactive_status]
    
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'slug')



admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(CommentBlog)
