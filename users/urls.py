from django.urls import path
from .views import RegisterView, ProfileView, UserListView, UserTokenObtainView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("login/", UserTokenObtainView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", ProfileView.as_view(), name="user-profile"),
    path("", UserListView.as_view(), name="user-list"),
]