import urllib3
from bs4 import BeautifulSoup

class Scraping():

    def __init__(self, url):
        self.url = url

    def grabData(self, filter):
        http = urllib3.PoolManager()
        r = http.request('GET', self.url)
        soup = BeautifulSoup(r.data, 'html.parser')

        titles = soup.find_all(class_="result-title")
        urls = soup.find_all('a', {"class": "result-title"}, href=True)
        hoods = soup.find_all(class_="result-hood")

        data = []
        for (title, url, hood) in zip(titles, urls, hoods):
            if filter.lower() not in str(title).lower():
                pass
            else:
                data.append(title.get_text() +" "+
                url['href'] + " "+ hood.get_text())
        return data
