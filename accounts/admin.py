from django.contrib import admin

from accounts.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','mobile_no','pincode']

admin.site.register(Customer,CustomerAdmin)