from django.urls import path
from userauth import views

app_name="user"

urlpatterns = [
    path("sign-up/",views.register_view,name="sign-up"),
    path("sign-in/",views.login_view,name="sign-in"),
    path("logout/",views.logout_view,name="logout"),
    path("profile/",views.profile,name="profile"),
    path("profile/update/",views.profile_update ,name="profile-update"),
    path("profile/password/", views.change_password, name="change_password"),
    path("profile/comments/", views.comments, name="comments"),
    path("deletecomments/<int:id>", views.deletecomments, name="deletecomments"),

]
