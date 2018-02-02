from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
# 注册自己创建的Model，使后台可以访问


class PostAdmin(admin.ModelAdmin):
	list_display = ['title','created_time','modified_time','category','author']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)