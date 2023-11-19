from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
STATUS_CHOICE= (
    ('process', 'Yönlendiriliyor'),
    ('shipped', 'Kargoda'),
    ('delivered', 'Teslim Ediliyor'),
)

STATUS= (
    ('disabled', 'Engellendi'),
    ('rejected', 'Reddedildi'),
    ('in_revie', 'İnceleniyor'),
    ('published', 'Yayınlandı'),
)
    
RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),  
    (4, '4'),
    (5, '5'),
)
    
def user_directory_path(instance, filename):
    return 'user{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def category_image(self):
        return mark_safe("<img src= '%s' width='50' height='50'/>"% (self.image.url)) #categorinin yanına resim eklemek için
   
    def __str__(self):
       return self.title
    
class Vendor(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path,default="urun.jpg")
    # description = models.TextField(null=True,blank=True,default="Satıcı")
    description = RichTextUploadingField(null=True,blank=True,default="Satıcı")
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now_add=True )
    address= models.CharField(max_length=100,default="Istanbul")
    contact = models.CharField(max_length=100,default="555 555 55 55")
    chat_resp_time = models.CharField(max_length=100,default="100")
    shipping_on_time = models.CharField(max_length=100,default="100")
    authentic_rating = models.CharField(max_length=100,default="100")
    days_return = models.CharField(max_length=100,default="100")
    warranty_period = models.CharField(max_length=100,default="100")
    
    class Meta:
        verbose_name_plural = "Vendors"
        
    def vendor_image(self):
        return mark_safe("<img src= '%s' width='50' height='50'/>"% (self.image.url)) #categorinin yanına resim eklemek için
   
    def __str__(self):
       return self.title
   
class Tags(models.Model):
    pass
   
class Product(models.Model):

    
    category = models.ForeignKey(Category,on_delete=models.CASCADE) # Category tablosuyla ilişki kurulması
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL,null=True,related_name="vendor")
    
    title = models.CharField(max_length=100,default="Taze Meyve")
    image = models.ImageField(upload_to=user_directory_path,default="urun.jpg")
    description = RichTextUploadingField(null=True,blank=True,default="Bu bir ürün")
    
    price = models.DecimalField(max_digits=9999999, decimal_places=2,default="1.99")
    old_price = models.DecimalField(max_digits=9999999, decimal_places=2,default="2.99")
    specifications =  RichTextUploadingField(null=True,blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.CASCADE, null=True)
    product_status = models.CharField(choices=STATUS,max_length=10,default="in_revie")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(null=True,blank=True)
    
    
    class Meta:
        verbose_name_plural = "Products"
        
    def product_image(self):
        return mark_safe("<img src= '%s' width='50' height='50'/>"% (self.image.url)) #categorinin yanına resim eklemek için
   
    def __str__(self):
       return self.title
    
    def get_precentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product_images",default="urun.jpg")
    product = models.ForeignKey(Product,related_name="p_images" ,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Images"
        
############################### Cart, Order,Order Items and Address########################
############################### Cart, Order,Order Items and Address########################
############################### Cart, Order,Order Items and Address########################

class CartOrder(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999, decimal_places=2,default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE,max_length=30,default="process")
    
    class Meta:
        verbose_name_plural = "Cart Order"

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder , on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    invoice_no = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999, decimal_places=2,default="1.99")
    total = models.DecimalField(max_digits=9999999, decimal_places=2,default="1.99")

    class Meta:
        verbose_name_plural = "Cart Order Items"
    def order_img(self):
        return mark_safe("<img src= '/media/%s' width='50' height='50'/>"% (self.image.url)) #categorinin yanına resim eklemek için
    
    
############################### Product Review , Wishlist and Address########################
############################### Product Review , Wishlist and Address########################
############################### Product Review , Wishlist and Address########################

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING)
    date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Product Reviews"
    
   
    def __str__(self):
       return self.product.title
   
    def get_rating(self):
       return self.rating

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Wishlist"
    
   
    def __str__(self):
       return self.product.title

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=100,null=True)
    status = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Address"
       