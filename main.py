from Scraping import Scraping
from Sms import Sms
import sys

#contact phone
phone = ""
#twilio voip number
twilio = ""
#twilio account sid
account = ""
#twilio auth token
token = ""

def main():
    sms = Sms(account, token, phone, twilio)
    scrape = Scraping(sys.argv[1])
    results = scrape.grabData(sys.argv[2])

    sms.sendSms(results)

if __name__ == "__main__":
    main()