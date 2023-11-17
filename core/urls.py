from django.urls import path
from core.views import index,shop



app_name = "core"

urlpatterns = [
    path('',index,name="index"),
    path('shop/',shop,name="shop"),
]

