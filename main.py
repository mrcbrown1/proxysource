import proxysource

urls = ["https://free-proxy-list.net/", "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt"]
proxy_modules = []

for url in urls:
    proxy_modules.append(proxysource.obtain_proxysearch(url))

for proxy in proxy_modules:
    out = proxy.get_proxies()
    print(out)

