import requests, pandas

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.kiwi_end_point = "https://api.tequila.kiwi.com/"
        #self.search = f"{self.kiwi_end_point}locations/id"
        self.kiwi_search_location = f"{self.kiwi_end_point}locations/id"
        self.kiwi_search_query = f"{self.kiwi_end_point}locations/query"
        self.kiwi_search_header = {
            "Content-Type": "application/json",
            "apikey": "snFD65bdvw4zbq2q_dWidQLvUxVAoHPj",
        }
        self.sheety_header = {
            "Authorization": "Bearer k#a(tIh7#0&LhSM"
        }
        self.sheety_endpoint = "https://api.sheety.co/8a0f13d5abe7fc3739822687ddf167a1/flightDeals/prices"
        self.data = self.pandas_get()
        self.validate_sheet_data()
        # sheet_data
        # {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
        # {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
        # {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
        # {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
        # {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
        # {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
        # {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
        # {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
        # {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]}


    # search location by IATA airport > this is the exact IATA airport or ISO3166 location code - station, airport,
    # city, autonomous_territory, subdivision, country, region, continent.
    # Multiple ids can be specified by appending &id={id}.

    def pandas_get(self):
        # print("Getting sheet")
        with open("Flight_Deals_prices.csv", "r") as file:
            data = pandas.read_csv(file)
        return data

    def validate_sheet_data(self):
        # print(self.data)
        for (row, i) in self.data.iterrows():
            # print(i.get('IATA Code'))
            if str(i.get('IATA Code')) == 'nan':
                # print(i.get('IATA Code'), row, i)
                city = i.get("City")
                iata = self.check_iatacode(i.get("City"))
                self.update_iatacode(row=row, city=city, code=iata)
        # self.sheet_data = self.pandas_get()
        # print(self.sheet_data)

    def update_iatacode(self, row, city, code):
        # print('updating DF')
        # print(row, city, code)
        for (index, data) in self.data.iterrows():
            if str(data.get('City')) == city:
                # print("updating Value")
                self.data.loc[row, 'IATA Code'] = code
                # print(self.data)
        # print("Updating File")
        with open("Flight_Deals_prices.csv", "w") as file:
            self.data.to_csv(file, index=False)

    def check_iatacode(self, city):
        # print(city)
        query = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=self.kiwi_search_query, params=query, headers=self.kiwi_search_header)
        response.raise_for_status()
        data = response.json()
        # print(data)
        return data['locations'][0]['code']