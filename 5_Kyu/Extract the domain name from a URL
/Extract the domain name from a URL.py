import re
def domain_name(url):
    print(url)
    url = url.replace('www', '')
    url = url.replace('https', '')
    url = url.replace('http', '')
    s = re.findall("[\s]?([']?[A-Za-z0-9]+'?[A-Za-z0-9'-]*)[\s,:]?", url)
    return s[0]

