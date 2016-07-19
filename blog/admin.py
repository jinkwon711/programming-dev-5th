from django.contrib import admin
from blog.models import Post
from blog.models import Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
class TagAdmin(admin.ModelAdmin):
    list_display = ['category']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
