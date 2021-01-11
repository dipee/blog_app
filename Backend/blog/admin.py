from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


class BlogPostAdmin(SummernoteModelAdmin):  
    summernote_fields = ('content')

admin.site.register(BlogPost, BlogPostAdmin)