from proxysource.base_proxy import base_proxy
from proxysource import utils
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
                params = string.split(" ")[1]

                if params[-1] == '!':
                    continue

                if string[-1] == '+':
                    google_passed = True
                elif string[-1] == '-':
                    google_passed = False
                else:
                    google_passed = False


                if params[-2:] == '-S':
                    https = True
                else:
                    https = False

                if len(params) == 6:
                    # We have all parameters present here
                    if params[-2:] == '-S':
                        https = True
                    else:
                        https = False

                    if params[-3:-2] == 'N':
                        anon = 1
                    elif params[-3:-2] == 'A':
                        anon = 2
                    elif params[-3:-1] == 'H':
                        anon = 3
                    else:
                        anon = 4

                    country = params[0:2]

                if len(params) == 4:
                    # with 4 characters, we are missing 1 of the three parameters. Country, anonymity, ssl
                    # First split on hyphen, and if the length of element 0 is 2, then that is the country.

                    params = params.split('-')
                    if len(params[0]) == 2:
                        country = params[0]

                        if params[1] == 'N':
                            https = False
                            anon = 1

                        if params[1] == 'A':
                            https = False
                            anon = 2

                        if params[1] == 'H':
                            https = False
                            anon = 3

                        if params[1] == 'S':
                            https = True
                            anon = 0

                    else:
                        # As first character was not two long, we are missing country.
                        country = 'XX' # Default value if unknown

                        if params[0] == 'N':
                            anon = 1
                        elif params[0] == 'A':
                            anon = 2
                        elif params[0] == 'H':
                            anon = 3
                        else:
                            anon = 4

                        if params[1] == 'S':
                            https = True
                        else:
                            https = False


                thisIP = {
                    'ip': ip,
                    'port': port,
                    'google': google_passed,
                    'https': https,
                    'anon': anon,
                    'country': country
                }

                dict_out[str(iter)] = thisIP
                iter = iter + 1

            dict_out = {
                'data_valid': True,
                'data': dict_out
            }


            if not utils.checkReturnDataStructure(dict_out):
                raise Exception("Incorrect packet structure found")

            return dict_out

        else:
            base_proxy.pageNotRetrieved()
