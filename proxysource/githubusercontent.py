from proxysource.base_proxy import base_proxy


class githubusercontent(base_proxy):

    def __init__(self, url=None):
        base_proxy.__init__(self, url)

    def get_proxies(self):
        return "Wow, really?"
