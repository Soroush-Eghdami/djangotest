from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogList.as_view(), name='list-blog'),
    path('/<int:pk>/<slug:slug>', BlogDetail.as_view(), name='detail-blog'),
    path('dashboard/list', BlogDashboardList.as_view(), name='list-blog-dashboard'),
    path('dashboard/category/list', BlogCategoryDashboardList.as_view(), name='list-blog-category-dashboard'),
    path('dashboard/category/create', BlogCategoryDashboardCreate.as_view(), name='create-blog-category-dashboard'),
    path('dashboard/category/update/<int:pk>/', BlogCategoryDashboardUpdate.as_view(), name='update-blog-category-dashboard'),
    path('dashboard/category/delete/<int:pk>/', BlogCategoryDashboardDelete.as_view(), name='delete-blog-category-dashboard'),
    path('dashboard/create', BlogDashboardCreate.as_view(), name='create-blog-dashboard'),
    path('dashboard/update/<int:pk>/', BlogDashboardUpdate.as_view(), name='update-blog-dashboard'),
    path('dashboard/delete/<int:pk>/', BlogDashboardDelete.as_view(), name='delete-blog'),
    
]