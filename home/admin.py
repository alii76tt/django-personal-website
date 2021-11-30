from django.contrib import admin
from .models import *

# Register your models here.


class HomeAdmin(admin.ModelAdmin):

    list_display = ['name', 'create_at', 'image_tag', 'status']
    list_display_links = ['name', 'image_tag', 'create_at', ]
    list_filter = ['create_at']
    search_fields = ['name']
    list_editable = ('status',)

    class Meta:
        model = Home


admin.site.register(Home, HomeAdmin)
admin.site.register(Social)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Interest)
admin.site.register(AwardAndCertifica)
admin.site.register(Contact)
admin.site.register(Setting)
