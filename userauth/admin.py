from django.contrib import admin
from .models import Profile,ContantUs

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=['full_name','phone']
    
class ContantUsAdmin(admin.ModelAdmin):
    list_display=['full_name','subject']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(ContantUs,ContantUsAdmin)