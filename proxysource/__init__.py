from importlib import import_module
from proxysource import base_proxy
from proxysource import utils

def obtain_proxysearch(url, *args, **kwargs):

    try:
        domain = utils.getHostnameFromURL(url)

        module_name = domain
        class_name = domain

        proxy_module = import_module('.' + str(module_name), package='proxysource')

        proxy_class = getattr(proxy_module, class_name)

        instance = proxy_class(url, *args, **kwargs)
        #instance = proxy_class(*args, **kwargs)

    except:
        raise Exception("Well we shit the bed!")

    return instance

def inc(x):
    return x+1