from abc import abstractmethod, ABCMeta
'''
Abstract class definition for a proxy website object. This defines how to interact with a proxy website, 
and what it returns.
'''


class base_proxy():
    __metaclass__ = ABCMeta

    def __init__(self, url=None):
        if url:
            self.url = url

    @abstractmethod
    def get_proxies(self):
        '''
        This method will search the provided url and return a dict of proxies found. It is not responsible for
        verifying that the proxies are responsive.
        '''
        pass

    def pageNotRetrieved(self):
        print("Could not retrieve page due to network issue.")
