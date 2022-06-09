import requests
from pprint import pprint
import os

SHEET_ENDPOINT = "https://api.sheety.co/a65d37e4e4c4751b050905bbc69d2c13/myFlightDeals/prices"
HEADERS = {
    "Authorization":os.environ.get("AUTH"),
    "Content-Type":"application/json",
}
USR_ENDPOINT = os.environ.get("SHEET_ENd")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url=SHEET_ENDPOINT, headers=HEADERS)
        self.response.raise_for_status()

    def get_info(self):
        data = self.response.json()["prices"]
        return data

    def update(self,row_id,iata):
        changes = {
            "price": {
                "iataCode":iata,
            }
        }

        edit = requests.put(url=f"{SHEET_ENDPOINT}/{row_id}",json=changes,headers=HEADERS)
        edit.raise_for_status()

    def get_emails(self):
        mail_response = requests.get(url=USR_ENDPOINT,headers=HEADERS)
        mail_response.raise_for_status()
        mail_data = mail_response.json()["users"]
        return mail_data


