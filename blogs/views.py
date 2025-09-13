from pyexpat import model
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blogs.forms import BlogForm, CategoryForm
from blogs.models import Blog, BlogCategory

# Create your views here.

# class BlogList(TemplateView):
#     template_name = "./blogs/blogs.html"
    
class BlogList(ListView):
    template_name = "./blogs/blogs.html"
    model = Blog
    context_object_name = 'blogs'
    
    

class BlogDetail(DetailView):
    model = Blog
    template_name='./blogs/detail.html'
    context_object_name = 'blog'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        next_post = Blog.objects.filter(
            created_at__gt=blog.created_at, status=True
        ).order_by('created_at').first()

        previous_post = Blog.objects.filter(
            created_at__lt=blog.created_at, status=True
        ).order_by('-created_at').first()
        
        latest_post = Blog.objects.filter(
            status = True).order_by('-created_at')[:3]
        
        get_all_category = BlogCategory.objects.all()

        context['next_post'] = next_post
        context['previous_post'] = previous_post
        context['latest_post'] = latest_post
        context['get_all_category'] = get_all_category
        return context


    
class BlogDashboardList(ListView):
    template_name = './blogs/blog_list_dashboard.html'
    model = Blog
    context_object_name = 'blogs'

class BlogDashboardCreate(CreateView):
    template_name = './blogs/blog_create_dashboard.html'
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list-blog-dashboard')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BlogDashboardUpdate(UpdateView):
    template_name = "./blogs/blog_update_dashboard.html"
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list-blog-dashboard')


class BlogDashboardDelete(DeleteView):
    template_name = "./blogs/blog_delete_confirm_dashboard.html"
    model = Blog
    success_url = reverse_lazy('blog:list-blog-dashboard')
    
    
class BlogCategoryDashboardList(ListView):
    template_name = './blogs/blog_category_list_dashboard.html'
    model = BlogCategory
    context_object_name = 'blog_categories'
    

class BlogCategoryDashboardCreate(CreateView):
    template_name = './blogs/blog_create_category_dashboard.html'
    model = BlogCategory
    form_class = CategoryForm
    success_url = reverse_lazy('blog:list-blog-category-dashboard')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BlogCategoryDashboardUpdate(UpdateView):
    template_name = "./blogs/blog_update_category_dashboard.html"
    model = BlogCategory
    form_class = CategoryForm
    success_url = reverse_lazy('blog:list-blog-category-dashboard')


class BlogCategoryDashboardDelete(DeleteView):
    template_name = "./blogs/blog_delete_category_confirm_dashboard.html"
    model = BlogCategory
    success_url = reverse_lazy('blog:list-blog-category-dashboard')    
