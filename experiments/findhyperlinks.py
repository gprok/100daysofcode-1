import bs4
import requests
import re
import tldextract

url = input("type URL: ")
domains = {}

print("URL", url, "hyperlinks:")

page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, 'lxml')

for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
    ext = tldextract.extract(link['href'])
    domain = ''
    if ext.subdomain != '' and ext.subdomain != 'www':
        domain = ext.subdomain + '.'
    domain = domain + ext.domain + '.' + ext.suffix
    if domain in domains:
        domains[domain] += 1
    else:
        domains[domain] = 1

for domain in domains:
    print(domain, domains[domain])
