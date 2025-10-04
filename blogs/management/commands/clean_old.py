from django.core.management.base import BaseCommand
from django.utils import timezone
from blogs.models import *
from datetime import timedelta


class Command(BaseCommand):
    help = "delete the last 30 days blogs"
    def handle(self, *args, **kwargs):
        cutoff = timezone.now()-timedelta(days=20)
        oldpost = Blog.objects.filter(created_at__lt=cutoff)
        count = oldpost.count()
        oldpost.delete()
        self.stdout.write(self.style.SUCCESS(f'{count} old posts deleted'))
        