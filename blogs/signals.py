from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CommentBlog

@receiver(post_save, sender=CommentBlog)
def send_notif_to_user(sender, instance, created, **kwargs):
    if created:
        blog = instance.blog
        print (f'======================== blog is created {blog.title} ================================')
    