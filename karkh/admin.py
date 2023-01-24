from django.contrib import admin
from .models import Transformars
from django.contrib.auth.models import Group

class TransformarsAdmin(admin.ModelAdmin):   
    list_display = ('number','section_name','maintinance_name', 'capacity','status','fixed')
    readonly_fields=['id','addtime']
    search_fields = ('section_name','number','capacity')
    list_filter=('fixed',)


admin.site.register(Transformars,TransformarsAdmin)
admin.site.unregister(Group)
# Register your models here.
