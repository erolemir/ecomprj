from django.urls import path
from core.views import index,shop,vendor_list_view,urun_detay,vendor_detial_view



app_name = "core"

urlpatterns = [
    path('',index,name="index"),
    path('shop/',shop,name="shop"),
    path('vendors/',vendor_list_view,name="vendor-list"),
    path("vendors/<int:id>", vendor_detial_view, name="vendor_detial"),
    path("products/<int:id>", urun_detay, name="urun_detay"),
]

