import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get('AT_USERNAME')   
api_key = os.environ.get('AT_APIKEY')


africastalking.initialize(username, api_key)

sms = africastalking.SMS

class SMSClient:
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message

    def send_sms(self):
        sms.send(self.message, [self.phone_number], callback=on_finish)
        

def on_finish(error, response):
    if error is not None:
        raise error
    print(response)
