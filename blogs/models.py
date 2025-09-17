from django.db import models
from django.contrib.auth import get_user_model
from .utils import image_upload_blog
from extentions.utils import jalali_converter
# Create your models here.

Users = get_user_model()

class BlogCategory(models.Model):
    name = models.CharField(verbose_name='دسته بندی')
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')
    status = models.BooleanField(default=True, verbose_name='وضعیت نمایش')
    
    def __str__(self):
        return f'{self.name}'
    
    def jcreated_at(self):  
        return jalali_converter(self.created_at)

class Blog(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=255)
    slug = models.SlugField(unique=True)
    desc = models.TextField(verbose_name='توضیحات کوتاه')
    category = models.ManyToManyField(BlogCategory,related_name='category', verbose_name='دسته بندی')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='کاربر')
    content = models.TextField(verbose_name='توضیحات')
    img = models.ImageField(upload_to=image_upload_blog)
    status = models.BooleanField(default=True, verbose_name='وضعیت نمایش')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شدده در')
    updated_at = models.DateTimeField(auto_now = True, verbose_name='بروز شده در')
    
    def __str__(self):
        return f'{self.title} | {self.user}'
    
    def jcreated_at(self):  
        return jalali_converter(self.created_at)
    

class CommentBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='author')
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} | {self.blog.title[:10]}'