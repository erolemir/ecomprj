from django.contrib import admin
from core.models import Category,CartOrderItems,Address,CartOrder,Wishlist,Vendor,Product,ProductImages,ProductReview
# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user','title','price','product_image','featured','product_status']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','category_image']
    
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','vendor_image']
    
class CatOrderAdmin(admin.ModelAdmin):
    list_display = ['user','price','paid_status','order_date','product_status']

class CatOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','invoice_no','item','image','qty','price','total']
    
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review','rating']
    
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product','date']
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address','status']
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(CartOrder,CatOrderAdmin)
admin.site.register(CartOrderItems,CatOrderItemsAdmin)
