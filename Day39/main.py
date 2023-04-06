#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager_obj = DataManager()

search_flight = FlightSearch(data_manager_obj.kiwi_search_header, 'MAA')
notify_user = NotificationManager()
for (row, i) in data_manager_obj.data.iterrows():
    iata = i.get('IATA Code')
    # if i.get('IATA Code') != 'SGC':
    #     continue
    # print(i.get('IATA Code'))
    flights = search_flight.search_using_iatacode(iata)
    if len(flights.get('data')) == 0:
        flights = search_flight.search_using_iatacode(iata, max_stop=1)
        flight_data_manipulate = FlightData()
        flight_data_manipulate.stop_overs = 1
    else:
        flight_data_manipulate = FlightData()
    # print(flights)
    your_price = i.get("Lowest Price")
    for j in flights['data']:
        flight_price = j["price"]
        if flight_price <= your_price:
            if flight_data_manipulate.stop_overs == 1:
                flight_data_manipulate.via_city = j['route'][0]['cityTo']
            data = flight_data_manipulate.process_data(**j)
            # print(data)
            notify_user.notify(data)
