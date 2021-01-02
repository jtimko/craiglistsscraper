import urllib3
from bs4 import BeautifulSoup


http = urllib3.PoolManager()
r = http.request('GET', 'https://sfbay.craigslist.org/search/msa?')

soup = BeautifulSoup(r.data, 'html.parser')

titles = soup.find_all(class_="result-title")
urls = soup.find_all('a', {"class": "result-title"}, href=True)
hoods = soup.find_all(class_="result-hood")

for i, (title, url, hood) in enumerate(zip(titles, urls, hoods), start=1):
    print("{} {} {} {}".format(str(i), title.get_text(), url['href'], hood.get_text()))
