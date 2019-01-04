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
    if ext.domain in domains:
        domains[ext.domain] += 1
    else:
        domains[ext.domain] = 1

for domain in domains:
    print(domain, domains[domain])
