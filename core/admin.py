from django.contrib import admin
from .models import Contact_us
# Register your models here.
admin.site.site_header = "My Shop Admin"
admin.site.site_title = "My Shop Admin Portal"
admin.site.index_title = "Welcome to My Shop Admin Portal"


admin.site.register(Contact_us)
