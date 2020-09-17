from django.contrib import admin
from .models import Profile, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'product_name', 'product_description', 'product_details', 'price', 'category', 'posted_on')
    date_hierarchy = 'posted_on'

admin.site.register(Profile),
admin.site.register(Post, PostAdmin)
