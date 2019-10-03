import proxysource

url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt'

a = proxysource.obtain_proxysearch(url)

print(a.get_proxies())

print(a.url)