from proxysource.base_proxy import base_proxy
from proxysource import utils
import requests
from lxml import html
'''
Template file, do not edit.
When copying, change class name to reflect new class.
Filename of new class should match class name.
'''

class freeproxylist(base_proxy):

    def __init__(self, url=None):
        base_proxy.__init__(self, url)

    def get_proxies(self):
        page = requests.get(self.url)

        if page.status_code == 200:
           tree = html.fromstring(page.content)

           try:
               rows = tree.xpath('//table[@id="proxylisttable"]/tbody/tr')
               out = {}
               iter = 0

               for row in rows:
                   proxy_info = row.xpath('.//td/text()')
                   # Ip, Port, Country Code, Country Name, Anon, Google, Https, Last Checked

                   country_code = proxy_info[2]
                   anon = proxy_info[4]

                   thisIP = {
                       'ip': proxy_info[0],
                       'port': proxy_info[1],
                       'google': proxy_info[5],
                       'https': proxy_info[6]
                   }

                   out[str(iter)] = thisIP
                   iter += 1

           except:
               out = "Error finding rows using xpath"



        else:
            base_proxy.pageNotRetrieved()
            out = "error"

        return out