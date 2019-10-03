import re
import ipaddress

def getHostnameFromURL(url):
    components = re.split('\.|\/', url)

    known_TLDs = ['com', 'net', 'org', 'co', 'biz']
    current_index = 0
    for item in components:
        if item in known_TLDs:
            break
        current_index += 1
    try:
        domain = components[current_index-1]
    except:
        raise Exception("Could not determine domain from URL.")

    return domain


def removeForbiddenChars(string):
    forbidden_chars = ['-']

    for char in forbidden_chars:
        string = string.replace(char, '')

    return string

def isIPAddress(ipAdress):
    try:
        ipaddress.ip_address(ipAdress)
        return True
    except:
        return False