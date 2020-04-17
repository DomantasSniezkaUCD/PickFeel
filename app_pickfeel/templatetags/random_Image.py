import os
import random
from django import template
from django.conf import settings

# module-level variable
register = template.Library()


@register.simple_tag
def random_images_category1(count=3):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    rand_dir = '/static/app_pickfeel/images/normal/'
    path = '/app_pickfeel/static/app_pickfeel/images/normal/'

    files = [f for f in os.listdir(settings.BASE_DIR + path)
             if f[f.rfind("."):] in valid_extensions]

    print(random.sample(files, count))
    return [rand_dir + filename for filename in random.sample(files, count)]


@register.simple_tag
def random_images_category2(count=9):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    rand_dir = '/static/app_pickfeel/images/mania/'
    path = '/app_pickfeel/static/app_pickfeel/images/mania/'

    files = [f for f in os.listdir(settings.BASE_DIR + path)
             if f[f.rfind("."):] in valid_extensions]

    print(random.sample(files, count))
    return [rand_dir + filename for filename in random.sample(files, count)]


@register.simple_tag
def random_images_category3(count=9):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    rand_dir = '/static/app_pickfeel/images/depression/'
    path = '/app_pickfeel/static/app_pickfeel/images/depression/'

    files = [f for f in os.listdir(settings.BASE_DIR + path)
             if f[f.rfind("."):] in valid_extensions]

    print(random.sample(files, count))
    return [rand_dir + filename for filename in random.sample(files, count)]