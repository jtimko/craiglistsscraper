from twilio.rest import Client

class Sms:
    def __init__(self, account, token, phone, twilio):
        self.account = account
        self.token = token
        self.phone = phone
        self.twilio = twilio
        self.client = Client(self.account, self.token)

    def sendSms(self, data):
        self.client.messages.create(to=self.phone, from_=self.twilio,
                                 body=data)