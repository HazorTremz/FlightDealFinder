import os

import requests
from datetime import datetime,timedelta
from pprint import pprint

SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
KEY = os.environ.get("KEY_FLIGHT")
HEADERS = {
    "apikey": KEY,
}
today = datetime.now()
tomorrow = today+timedelta(days=1)
end_date = tomorrow+timedelta(days=6*30)
min_return = tomorrow+timedelta(days=6)
max_return = tomorrow+timedelta(days=27)


class FlightData:
    #This class is responsible for structuring the flight data.
    def get_flight_details(self,city_code):
        search_params = {
            "fly_from":"LON",
            "fly_to":city_code,
            "date_from":tomorrow.strftime("%d/%m/%Y"),
            "date_to":end_date.strftime("%d/%m/%Y"),
            "return_from":min_return.strftime("%d/%m/%Y"),
            "return_to":max_return.strftime("%d/%m/%Y"),
            "curr":"GBP",
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,

        }
        search_response = requests.get(url=SEARCH_ENDPOINT, params=search_params, headers=HEADERS)
        search_response.raise_for_status()
        try:
            flight_data = search_response.json()["data"][0]
        except IndexError:
            search_params["max_stopovers"] = 1
            search_response = requests.get(url=SEARCH_ENDPOINT, params=search_params, headers=HEADERS)
            flight_data = search_response.json()["data"][0]
            return flight_data
        else:
            return flight_data


