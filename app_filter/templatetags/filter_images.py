import os
import random
from django import template
from django.conf import settings

# module-level variable
register = template.Library()


@register.simple_tag
def filter_images_normal(count=3):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    rand_dir = '/static/app_filter/images/normal/'
    path = '/app_filter/static/app_filter/images/normal/'

    files = [f for f in os.listdir(settings.BASE_DIR + path)
             if f[f.rfind("."):] in valid_extensions]

    print(random.sample(files, count))
    return [rand_dir + filename for filename in random.sample(files, count)]

# @register.simple_tag
# def filter_images_mania(count=3):
#     valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
#     rand_dir = '/static/app_filter/images/mania/'
#     path = '/app_filter/static/app_filter/images/mania/'
#
#     files = [f for f in os.listdir(settings.BASE_DIR + path)
#              if f[f.rfind("."):] in valid_extensions]
#
#     # print(random.sample(files, count))
#     print(rand_dir)
#     return [rand_dir + filename for filename in random.sample(files, count)]
#
#
#
# @register.simple_tag
# def filter_images_depression(count=3):
#     valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
#     rand_dir = '/static/app_filter/images/depression/'
#     path = '/app_filter/static/app_filter/images/depression/'
#
#     files = [f for f in os.listdir(settings.BASE_DIR + path)
#              if f[f.rfind("."):] in valid_extensions]
#
#     # print(random.sample(files, count))
#
#     return [rand_dir + filename for filename in random.sample(files, count)]
