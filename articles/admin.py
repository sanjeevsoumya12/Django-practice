from django.contrib import admin

# Register your models here.
from .models import Article

#this class is create to show id & title    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id","title"]
    search_fields = ['title','content'] # for create a search field in admin

admin.site.register(Article,ArticleAdmin)