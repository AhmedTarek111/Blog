from django.contrib import admin
from .models import Post,Comment
from django_summernote.admin import SummernoteModelAdmin

class CommentAdmin(SummernoteModelAdmin):
    summernote_fields= 'content'
    list_display = ['title','content','create_date','draft','tags','image','author']
    search_fields = ['content','tags','title','author']
    list_filter =['author',]
admin.site.register(Post,CommentAdmin)
admin.site.register(Comment)
