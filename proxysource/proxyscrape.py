from proxysource.base_proxy import base_proxy
from proxysource import utils
import requests

class proxyscrape(base_proxy):

    def __init__(self, url=None):
        base_proxy.__init__(self, url)

    def get_proxies(self):
        out = {
            'data_valid': False,
            'data': {}
        }

        page = requests.get(self.url)

        iter = 0

        if page.status_code == 200:
            for line in page.text.splitlines():
                ipAddr = line.split(':')
                port = ipAddr[1]
                ipAddr = ipAddr[0]
                params = utils.getPHPParams(self.url)

                if params['ssl'] is not None:
                    ssl = True if params['ssl'] == 'yes' else False
                else:
                    ssl = False

                anon = 0

                if params['anonymity'] is not None:
                    if params['anonymity'] == 'elite':
                        anon = 3
                    elif params['anonymity'] == 'anonymous':
                        anon = 2
                    elif params['anonymity'] == 'transparent':
                        anon = 1

                thisIP = {
                    'ip': ipAddr,
                    'port': port,
                    'google': False,
                    'https': ssl,
                    'anon': anon,
                    'country': 'XX'
                }

                out['data'][str(iter)] = thisIP
                iter += 1
            out['data_valid'] = True

            if not utils.checkReturnDataStructure(out):
                raise Exception("Incorrect packet structure found")


        else:
            base_proxy.pageNotRetrieved()



        return out
