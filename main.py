from Scraping import Scraping
from Sms import Sms
import sys

#contact phone
phone = "+"
#twilio voip number
twilio = "+"
#twilio account sid
account = ""
#twilio auth token
token = ""

def main(search_item):
    sms = Sms(account, token, phone, twilio)
    scrape = Scraping("https://sfbay.craigslist.org/d/musical-instruments/search/msa")
    results = scrape.grabData(search_item)
    sms.sendSms(results)
