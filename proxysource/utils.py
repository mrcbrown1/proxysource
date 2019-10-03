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

def checkReturnDataStructure(packet):

    '''
    This function is used to verify the data structure of proxy dicts before the module returns them. It can also be used externally.
    '''

    # First check whether it has the data valid key

    if 'data_valid' in packet.keys():
        # Then check it is set to true
        if packet['data_valid'] == True:
            # The check internal data structure
            passed = True
            expected_keys = ['ip', 'port', 'google', 'anon', 'country', 'https']

            data_items = len(packet['data'])
            for i in range(0,data_items-1):
                for key in expected_keys:
                    if key not in packet['data'][str(i)].keys():
                        passed = False

            return passed
    else:
        return False


def mergeResults(result_dicts):

    '''
    This function takes any number of result proxy lists and merges them into one flat structure
    '''

    output = {
        'data_valid': True,
        'data': {}
    }

    total_processed = 0

    for list in result_dicts:
        for i in range(0, len(list['data'])):
            output['data'][str(total_processed)] = list['data'][str(i)]
            total_processed += 1

    if not checkReturnDataStructure(output):
        raise Exception("Incorrect formatting of lists during a merge operation")

    return output

def makeListUnique(merged):
    IPs = merged['data']

    total_IPs = len(IPs)

    uniques = {}
    unique_count = 0
    seen = []
    for i in range(0,total_IPs):
        if IPs[str(i)]['ip'] not in seen:
            uniques[str(unique_count)] = IPs[str(i)]
            seen.append(IPs[str(i)]['ip'])
            unique_count += 1

    out = {
        'data_valid': True,
        'data': uniques
    }

    return out

def getPHPParams(url):

    '''
    This gets all the parameters passed to a php call and returns them as a dict
    '''

    output = {}

    params = url.split('?')

    params = params[1].split('&')

    for param in params:
        (key, value) = param.split('=')
        output[key] = value

    return output