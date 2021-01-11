import urllib3
from bs4 import BeautifulSoup

class Scraping():

    def __init__(self, url):
        self.url = url

    def grabData(self):
        http = urllib3.PoolManager()
        r = http.request('GET', self.url)
        soup = BeautifulSoup(r.data, 'html.parser')

        ids = soup.find_all(attrs={"data-id": True})
        titles = soup.find_all(class_="result-title")
        urls = soup.find_all('a', {"class": "result-title"}, href=True)
        hoods = soup.find_all(class_="result-hood")

        data = []
        for (id, title, url, hood) in zip(ids, titles, urls, hoods):
            data.append(tuple((id.get_text(), title.get_text(), url['href'], hood.get_text())))
        return data
