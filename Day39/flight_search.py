import pprint

import requests, datetime
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, search_header, from_loc):
        self.kiwi_end_point = "https://api.tequila.kiwi.com/"
        self.kiwi_header = search_header
        self.from_loc = from_loc

    # search flight for next 6 months from now
    def search_using_iatacode(self, iata, max_stop=0):
        search_url = f"{self.kiwi_end_point}v2/search"
        date_from = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        date_to = date_from + datetime.timedelta(weeks=(4 * 6))
        query = {
            "fly_from": self.from_loc,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "fly_to": iata,
            "max_stopovers": max_stop,
        }
        response = requests.get(url=search_url, params=query, headers=self.kiwi_header)
        response.raise_for_status()
        data = response.json()
        return data
