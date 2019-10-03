from proxysource.base_proxy import base_proxy
import requests

class githubusercontent(base_proxy):

    def __init__(self, url=None):
        base_proxy.__init__(self, url)

    def get_proxies(self):
        page = requests.get(self.url)
        if page.status_code == 200:
            text = page.text
            lines = text.splitlines()
            ip_data = lines[9:-2]

            dict_out = {}
            iter = 0

            for string in ip_data:
                ip = string.split(" ")[0].split(":")[0]
                port = string.split(" ")[0].split(":")[1]
                if string[-1] == '+':
                    google_passed = True
                elif string[-1] == '-':
                    google_passed = False
                else:
                    google_passed = False

                params = string.split(" ")[1]
                if params[-2:] == '-S':
                    https = True
                else:
                    https = False

                thisIP = {
                    'ip': ip,
                    'port': port,
                    'google': google_passed,
                    'https': https
                }

                dict_out[str(iter)] = thisIP
                iter = iter + 1

            return dict_out

        else:
            base_proxy.pageNotRetrieved()
