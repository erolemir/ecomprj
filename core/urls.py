from django.urls import path
from core.views import index,shop,vendor_list_view



app_name = "core"

urlpatterns = [
    path('',index,name="index"),
    path('shop/',shop,name="shop"),
    path('vendors/',vendor_list_view,name="vendor-list"),
]

