from django.urls import path
from user import views

app_name="user"

urlpatterns = [
    path("sign-up/",views.register_view,name="sign-up")
]
