from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def jinja2_environ(**options):
    """ Jinja2 Environment """
    # Create an object of the environment
    env = Environment(**options)

    # Customize methods, such as: {{ static('relative path of static file') }}, {{ url('the namespace of route') }}
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })

    return env
