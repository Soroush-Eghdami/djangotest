from django import forms

from blogs.models import Blog, BlogCategory

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('created_at', 'updated_at', 'user')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        exclude = ('created_at', 'updated_at')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }