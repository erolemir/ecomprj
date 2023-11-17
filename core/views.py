from django.shortcuts import render,HttpResponse
from core.models import Category,CartOrderItems,Address,CartOrder,Wishlist,Vendor,Product,ProductImages,ProductReview
from django.contrib.auth.decorators import login_required


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

def vendor_list_view(request):
    vendors= Vendor.objects.all()
    context ={
        "vendors":vendors,
    }
    return render(request,"core/vendor-list.html",context)


