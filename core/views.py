from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = "./core/home.html"
    

class AdminView(TemplateView):
    template_name = "./core/admin.html" 
    
    
class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("core:contact")  # redirect after success

    def form_valid(self, form):
        form.save()  # saves the message to DB
        return super().form_valid(form)