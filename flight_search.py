import requests

SHEET_ENDPOINT = "https://api.sheety.co/284278c5d757ef8dad6843e2345be840/flightDeals/prices"
DATA = {
    "price": {
        "iataCode": "TESTING"
    }
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, cities):
        self.cities = cities

    def do(self):
        for city in self.cities:
            print(city[1])
            row_endpoint = f"{SHEET_ENDPOINT}/{city[1]}"  # (city, id) -> [1] is the id
            response = requests.put(url=row_endpoint, json=DATA)

            print(response.json())
