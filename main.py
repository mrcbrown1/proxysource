import proxysource

urls = ["https://free-proxy-list.net/",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3800&country=all&ssl=yes&anonymity=elite",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3800&country=all&ssl=yes&anonymity=anonymous",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3800&country=all&ssl=yes&anonymity=transparent",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3800&country=all&ssl=no&anonymity=elite",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3800&country=all&ssl=no&anonymity=anonymous",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=3800&country=all&ssl=no&anonymity=transparent"
        ]


proxy_modules = []

for url in urls:
    try:
        proxy = proxysource.obtain_proxysearch(url)
        proxy_modules.append(proxy)
    except:
        print("WARNING: could not obtain proxy handler for: " + url)

out = []

for proxy in proxy_modules:
    temp = proxy.get_proxies()
    print(temp)
    if temp['data_valid']:
        out.append(temp)

merged = proxysource.utils.mergeResults(out)
uniques = proxysource.utils.makeListUnique(merged)
print(merged)
print(str(len(merged['data'])) + " IPs found")

print(uniques)
print(str(len(uniques['data'])) + " unique IPs found")

