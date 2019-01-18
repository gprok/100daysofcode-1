import bs4
import requests
import re
import tldextract

class Href:
    """ Extracts information form a given URL """
    def __init__(self, url):
        self.url = url
        page = requests.get(url)
        self.soup = bs4.BeautifulSoup(page.text, 'lxml')

    def getHyperlinks(self):
        return self.soup.findAll('a', attrs={'href': re.compile("^http")})

    def countHyperlinks(self):
        domains = {}
        hyperlinks = self.getHyperlinks()
        for link in self.soup.findAll('a', attrs={'href': re.compile("^http")}):
            ext = tldextract.extract(link['href'])
            domain = ''
            if ext.subdomain != '' and ext.subdomain != 'www':
                domain = ext.subdomain + '.'
            domain = domain + ext.domain + '.' + ext.suffix
            if domain in domains:
                domains[domain] += 1
            else:
                domains[domain] = 1
        return domains
