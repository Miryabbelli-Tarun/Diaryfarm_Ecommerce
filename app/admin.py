from django.contrib import admin

from app.models import Cart, OrderPlaced, Product, Wishlist

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','discount_price','selling_price','category']
admin.site.register(Product,ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
admin.site.register(Cart,CartAdmin)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','ordered_date','quantity','status']
admin.site.register(OrderPlaced,OrderPlacedAdmin)

class WishlistAdmin(admin.ModelAdmin):
    list_display=['id','user','product']
admin.site.register(Wishlist,WishlistAdmin)