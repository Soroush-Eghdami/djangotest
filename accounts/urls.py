from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update_profile', ProfileUpdateView.as_view(), name='update_profile'),
    path("users/", UserListView.as_view(), name="users-list"),   # 👈 matches template
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
]
