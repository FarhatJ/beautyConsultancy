from django.contrib import admin
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Category,CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Post, PostAdmin)
