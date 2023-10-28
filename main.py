import requests
from pprint import pprint
from flight_search import FlightSearch

SHEET_ENDPOINT = "https://api.sheety.co/284278c5d757ef8dad6843e2345be840/flightDeals/prices"

sheet_data = requests.get(SHEET_ENDPOINT).json()

cities = [(city['city'], city['id']) for city in sheet_data['prices']]

fs = FlightSearch(cities)

fs.do()
