from django.core.management.base import BaseCommand
from django.utils import timezone
from blogs.models import *
from datetime import timedelta
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = "Setup user groups and permissions"
    
    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Blog)
        authors,_ = Group.objects.get_or_create(name='Authors')
        authors.permissions.set([Permission.objects.get(codename='add_blog', content_type=content_type),
                                Permission.objects.get(codename='change_blog', content_type=content_type),])
        editors,_ = Group.objects.get_or_create(name='Editors')
        editors.permissions.set([Permission.objects.get(codename='add_blog', content_type=content_type),
                                Permission.objects.get(codename='change_blog', content_type=content_type),
                                Permission.objects.get(codename='delete_blog', content_type=content_type),])
        admins,_ = Group.objects.get_or_create(name='Admins')
        admins.permissions.set(Permission.objects.all())
        
        self.stdout.write(self.style.SUCCESS('Groups and permissions have been set up successfully.'))