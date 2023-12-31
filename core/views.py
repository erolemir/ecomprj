from audioop import avg
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from core.models import Category,CartOrderItems,Address,CartOrder,Wishlist,Vendor,Product,ProductImages,ProductReview
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Avg
from core.forms import ProductReviewForm
from django.contrib import messages
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.template.loader import render_to_string
from userauth.models import ContantUs

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
            cart_data[str(request.GET['id'])]['qty']= int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else :
            cart_data =request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else :
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({"data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})


def cart_view(request):

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for product_id,item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            
        return render(request,"core/cart.html",{"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']),'cart_total_amount':cart_total_amount})
    else:
        messages.warning(request,"Sepetiniz Boş")
        return redirect("core:index")
    
def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data
        
        
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for product_id,item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            
    context = render_to_string("core/async/cart-list.html",{"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']),'cart_total_amount':cart_total_amount,'product_id':product_id})
    return JsonResponse({"data":context,'totalcartitems': len(request.session['cart_data_obj'])})

def update_cart(request):
    product_id = str(request.GET['id'])
    product_qty = request.GET['qty']
    
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = product_qty
            request.session['cart_data_obj'] = cart_data
        
        
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for product_id,item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            
    context = render_to_string("core/async/cart-list.html",{"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']),'cart_total_amount':cart_total_amount,'product_id':product_id})
    return JsonResponse({"data":context,'totalcartitems': len(request.session['cart_data_obj'])})

def clear_cart(request):
    if 'cart_data_obj' in request.session:
        del request.session['cart_data_obj']
        request.session.modified = True
    return JsonResponse({'status': 'success'})

def checkout_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for product_id,item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            
            
        return render(request,"core/checkout.html",{"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']),'cart_total_amount':cart_total_amount})
    
def contact(request):
    return render(request,"core/contact.html")

def ajax_contact_form(request):
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    message = request.GET['message']
    subject = request.GET['subject']
    
    contact = ContantUs.objects.create(
        full_name=full_name,
        email = email,
        phone = phone,
        message = message,
        subject = subject,
        
    )
    data = {
        "bool": True,
        "message":"Mesaj başarıyla gönderildi",
    }
    return JsonResponse({"data":data})


def hakkimizda(request):
    return render(request,"core/hakkimizda.html")