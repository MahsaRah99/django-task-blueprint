# This file will get replaced in the review step with real sms functionality.
import logging
from dataclasses import dataclass
from kavenegar import KavenegarAPI, APIException, HTTPException

# @dataclass
# class SMS:
#     phone_number: str
#     message: str

#     def send(self):
#         logging.info(f'Sending {self.message} to {self.phone_number}')


def send_sms(phone_number, message):
    try:
        api = KavenegarAPI("my api key")
        params = {"sender": "my number", "receptor": phone_number, "message": message}
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
