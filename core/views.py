from django.shortcuts import render,HttpResponse
from core.models import Category,CartOrderItems,Address,CartOrder,Wishlist,Vendor,Product,ProductImages,ProductReview

# Create your views here.

def index(request):
    toprak = Category.objects.get(title="Toprakta Yetişen")
    products = Product.objects.filter(category=toprak)[:3]
    context = {
        'products':products
    }
    return render(request,'core/index.html',context)

def shop(request):
    products = Product.objects.filter(product_status="published")
    context = {
        "products":products,
    }
    return render(request, 'core/shop.html',context)

