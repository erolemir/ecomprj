from django.urls import path
from core.views import index,shop,vendor_list_view,urun_detay,vendor_detial_view,addcomment,search,product_search_auto,add_to_cart



app_name = "core"

urlpatterns = [
    path('',index,name="index"),
    path('shop/',shop,name="shop"),
    path('vendors/',vendor_list_view,name="vendor-list"),
    path("vendors/<int:id>", vendor_detial_view, name="vendor_detial"),
    path("products/<int:id>", urun_detay, name="urun_detay"),
    path("products/addcomment/<int:id>", addcomment, name="yorum_ekle"),
    path("search/", search, name="search"),
    path('search_auto/', product_search_auto, name='product_search_auto'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),

]

