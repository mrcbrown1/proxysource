from importlib import import_module
from proxysource import base_proxy
from proxysource import utils

def obtain_proxysearch(url, *args, **kwargs):

    try:
        domain = utils.removeForbiddenChars(utils.getHostnameFromURL(url))

        module_name = domain
        class_name = domain

        proxy_module = import_module('.' + str(module_name), package='proxysource')

        proxy_class = getattr(proxy_module, class_name)

        instance = proxy_class(url, *args, **kwargs)
        #instance = proxy_class(*args, **kwargs)

    except (AttributeError, ImportError):
        raise ImportError('{} cannot be handled by this tool.'.format(url))

    return instance