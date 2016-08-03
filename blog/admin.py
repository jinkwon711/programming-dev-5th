from django.contrib import admin
from blog.models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','author', 'message']

class TagAdmin(admin.ModelAdmin):
    list_display = ['category']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']
class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ['zipcode']
class Zip_CodeAdmin(admin.ModelAdmin):
    list_display = ['zip_code', 'city', 'gu', 'dong','road']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ZipCode, ZipCodeAdmin)
admin.site.register(Zip_Code, Zip_CodeAdmin)
admin.site.register(Comment, CommentAdmin)