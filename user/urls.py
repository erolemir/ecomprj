from django.urls import path
from user import views

app_name="user"

urlpatterns = [
    path("sign-up/",views.register_view,name="sign-up"),
    path("sign-in/",views.login_view,name="sign-in"),
    path("logout/",views.logout_view,name="logout"),
]
