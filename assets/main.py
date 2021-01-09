from assets.Scraping import Scraping
from assets.Sms import Sms
import sys
import time

#contact phone
loop = True
#twilio voip number
twilio = "+"
#twilio account sid
account = ""
#twilio auth token
token = ""

def main(search_item, phone, interval):
    last = None
    while loop:
        sms = Sms(account, token, phone, twilio)
        scrape = Scraping("https://sfbay.craigslist.org/d/for-sale/search/sss?sort=date&query={}".format(search_item))
        results = scrape.grabData()

        if last is None:
            last = results[0]
        elif last == results[0]:
            pass
        else:
            for r in results:
                if r is not last:
                    sms.sendSms(r)
                    print(r)
                else:
                    last = results[0]
                    break
            #sms.sendSms(results)
        time.sleep(interval)
