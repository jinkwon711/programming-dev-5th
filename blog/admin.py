from django.contrib import admin
from blog.models import Post, Tag, Contact, ZipCode
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

class TagAdmin(admin.ModelAdmin):
    list_display = ['category']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']
class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ['zipcode']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ZipCode, ZipCodeAdmin)