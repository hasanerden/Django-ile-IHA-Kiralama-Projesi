from django.contrib import admin
from .models import Airvehicles, Category
from django.utils.safestring import mark_safe

class IhaAdmin(admin.ModelAdmin):
    list_display = ("brand","model","weight","is_active","slug","categori_name")
    list_editable = ("is_active",)
    search_fields = ("brand","model","weight")
    list_filter = ("is_active","category")
    
    def categori_name(self, obj):
        html = ""
        for categori in Airvehicles.obj.category.all():
            html += "<li>" + categori.name + "</li>"

        html += "</ul>"        
        
        return mark_safe(html)   
    
admin.site.register(Airvehicles, IhaAdmin)
admin.site.register(Category)
