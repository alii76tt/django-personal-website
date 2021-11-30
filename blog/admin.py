from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'publishing_date', 'image_tag', ]
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title']
    list_editable = ('title',)

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
