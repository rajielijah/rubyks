from django.contrib import admin
from .models import Profile, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'product_name', 'product_description', 'product_details', 'price', 'category', 'posted_on')
    date_hierarchy = 'posted_on'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',  'company_name','user', 'gender', 'id')
admin.site.register(Profile, ProfileAdmin),
admin.site.register(Post, PostAdmin)
