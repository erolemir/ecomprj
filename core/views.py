from audioop import avg
import json
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.views import View
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


def search(request):
    query = request.GET.get("q")
    
    products = Product.objects.filter(title__icontains=query)
    
    context = {
        "products":products,
        "query":query,
        
    }
    return render(request,"core/search.html",context)

def product_search_auto(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = [product.title for product in products]
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def add_to_cart(request):
    cart_product ={}
    cart_product[str(request.GET['id'])] ={
        'title':request.GET['title'],
        'qty':request.GET['qty'],
        'price':request.GET['price'],
        'image':request.GET['image'],
    }
    
    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['gty']= int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else :
            cart_data =request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else :
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({"data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})
