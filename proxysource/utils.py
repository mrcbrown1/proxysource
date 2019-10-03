import re

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