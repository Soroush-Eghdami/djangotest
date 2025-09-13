from django.urls import path, include
from .views import HomeView, AdminView, ContactView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', AdminView.as_view()),
    path('contact/', ContactView.as_view(), name='contact'),
]
