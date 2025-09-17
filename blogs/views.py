from pyexpat import model
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blogs.forms import *
from blogs.models import *

# Create your views here.

# class BlogList(TemplateView):
#     template_name = "./blogs/blogs.html"
    
class BlogList(ListView):
    template_name = "./blogs/blogs.html"
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains = query) | queryset.filter(content__icontains = query)
        return queryset
    

class BlogDetail(DetailView):
    model = Blog
    template_name = './blogs/detail.html'
    context_object_name = 'blog'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        context['next_post'] = Blog.objects.filter(
            created_at__gt=blog.created_at, status=True
        ).order_by('created_at').first()

        context['previous_post'] = Blog.objects.filter(
            created_at__lt=blog.created_at, status=True
        ).order_by('-created_at').first()

        context['latest_post'] = Blog.objects.filter(
            status=True
        ).order_by('-created_at')[:3]

        context['get_all_category'] = BlogCategory.objects.all()

        # فرم کامنت
        context['form'] = CommentForm()

        return context
    
    def post(self, request, *args, **kwargs): 
        self.object = self.get_object() 
        form = CommentForm(request.POST) 
        if form.is_valid(): 
            comment = form.save(commit=False) 
            comment.blog = self.object 
            comment.user = request.user   # نیازمند login
            comment.save() 
            return redirect("blog:detail-blog", pk=self.object.pk, slug=self.object.slug) 
        context = self.get_context_data() 
        context["form"] = form 
        return self.render_to_response(context)



    
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
