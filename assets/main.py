from assets.Scraping import Scraping
from assets.Sms import Sms
import sys
import time

#contact phone
loop = True
#twilio voip number
twilio = "+1"
#twilio account sid
account = ""
#twilio auth token
token = ""

def main(search_item, phone, interval):
    last = list()
    
    while loop:
        sms = Sms(account, token, phone, twilio)
        scrape = Scraping("https://sfbay.craigslist.org/d/for-sale/search/sss?sort=date&query={}".format(search_item))
        results = scrape.grabData()

        if len(last) < 1:
            for r in results:
                last.append(r[0].rstrip())
        else:
            for r in results:
                if r[0].rstrip() in last:
                    pass
                else:
                    print("{} {} {}".format(r[1], r[2], r[3]))
                    last.append(r[0].rstrip())
                    #sms.sendSms("{} {} {}".format(r[1], r[2], r[3]))
        time.sleep(interval*60)
