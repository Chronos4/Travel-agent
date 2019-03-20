import os
import string
import random
from django.utils.text import slugify


# we get the filename by path


def get_filename(path):
    return os.path.basename(path)

# create random strings


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.last_name+instance.first_name)

    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug)
    if qs.exists():
        new_slug = f'{slug}-{random_string_generator(size=6)}'
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def unique_id_generator(instance):
    id = random_string_generator(size=11)
    Klass = instance.__class__
    while True:
        qs = Klass.objects.filter(unique_id=id)
        if qs.exists():
            id = random_string_generator(size=11)
        else:
            return id
