from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields':['title','content']}),
        ('Info', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    
    list_display = ('title','pub_date')
    list_filter = ['pub_date']
    search_fields = ['title','content']

admin.site.register(Post, PostAdmin)
