from django.contrib import admin
from .models import Category, Post, Comment, UserProfile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status', 'has_image']
    list_filter = ['status', 'created', 'publish', 'author', 'categories']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['-publish']
    fields = ['title', 'slug', 'author', 'content', 'featured_image', 'categories', 'status']
    
    def has_image(self, obj):
        return bool(obj.featured_image)
    has_image.boolean = True
    has_image.short_description = 'Has Image'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Fix: Change 'name' and 'email' to 'author' and 'post'
    list_display = ['author', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['content', 'author__username']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Fix: Remove 'location' and use fields that exist in UserProfile
    list_display = ['user', 'website']
    search_fields = ['user__username', 'bio']

