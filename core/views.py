from audioop import avg
from django.shortcuts import render,HttpResponse
from core.models import Category,CartOrderItems,Address,CartOrder,Wishlist,Vendor,Product,ProductImages,ProductReview
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Avg
from core.forms import ProductReviewForm
from django.contrib import messages
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

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

def urun_detay(request,id):
    product = Product.objects.get(pk=id)
    p_image = product.p_images.all()
    review = ProductReview.objects.filter(product=product)
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    context = {"product":product,
               "p_image":p_image,
               "average_rating":average_rating,
                "review":review,
    }
    return render(request, "core/urun_detay.html",context)


def vendor_detial_view(request,id):
    vendor = Vendor.objects.get(pk=id)
    
    # Yorumları getir

    context = {"vendor":vendor,
            
    }
    return render(request, "core/vendor_detial.html",context)


def addcomment(request,id):
    
    url = request.META.get('HTTP_REFERER') #get last url
    
    if request.method=='POST':
        form = ProductReviewForm(request.POST)

        if form.is_valid():
            current_user = request.user
            
            data= ProductReview()
            data.user_id= current_user.id
            data.product_id= id
            data.review= form.cleaned_data['review']
            data.rating= form.cleaned_data['rating']
            data.save()
            messages.success(request,"Yorumunuz başarıyla gönderilmiştir. Teşekkür ederiz.")
            
            return HttpResponseRedirect(url)
    messages.warning(request,"Yorumunuz Gönderilememiştir. Lütfen Kontrol Ediniz.")
    return HttpResponseRedirect(url)