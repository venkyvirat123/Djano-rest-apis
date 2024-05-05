from django.contrib import admin
from . models import BlogPost

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=["id","title","description","date_published"]

admin.site.register(BlogPost,BlogAdmin)
