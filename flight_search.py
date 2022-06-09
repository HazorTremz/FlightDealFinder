import os

import requests

KEY = os.environ.get("KEY_1")
LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
HEADERS = {
    "apikey": KEY,
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata(self,city):
        flight_params = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=LOCATION_ENDPOINT, params=flight_params, headers=HEADERS)
        response.raise_for_status()
        flight_data = response.json()["locations"]
        iata = flight_data[0]["code"]
        return iata