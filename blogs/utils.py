import time
from django.utils.text import slugify

def image_upload_blog(instance, filename):
    path = 'uploads/' + 'blog/' + slugify(instance.title, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title) + '-' + filename
    return path + '/' + name
