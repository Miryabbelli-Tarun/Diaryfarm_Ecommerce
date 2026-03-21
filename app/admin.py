from django.contrib import admin

from app.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','discount_price','selling_price','category']
admin.site.register(Product,ProductAdmin)