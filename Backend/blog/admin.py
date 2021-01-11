from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


class BlogPostAdmin(SummernoteModelAdmin):  
    exclude = ('slug',)
    list_display = ('id', 'title', 'category', 'date_created')
    list_display_links = ('id', 'title', 'category', 'date_created')
    search_fields = ('title',)
    list_per_page = 20
    summernote_fields = ('content')

admin.site.register(BlogPost, BlogPostAdmin)