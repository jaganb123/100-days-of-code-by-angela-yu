import pytz, datetime


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.stop_overs = 0
        self.via_city = ""

    def process_data(self, **kwargs):
        info_data = {}
        scratch = {
            "flyFrom": kwargs.get('flyFrom'),
            "flyTo": kwargs.get('flyTo'),
            "cityFrom": kwargs.get('cityFrom'),
            "cityTo": kwargs.get('cityTo'),
            "price": kwargs.get('price'),
            "airlines": kwargs.get('airlines'),
            "utc_arrival": kwargs.get("utc_arrival"),
            "utc_departure": kwargs.get("utc_departure"),
            "stop_over": self.stop_overs,
            "via_city": self.via_city,
        }
        book_url = f"https://www.google.co.uk/flights?hl=en#flt={scratch.get('flyFrom')}.{scratch.get('flyTo')}.2020-08-25*SXF.STN.2020-09-08"
        scratch.update({"arrival_tz": self.change_date_format(scratch['utc_arrival']),
                                     "departure_tz": self.change_date_format(scratch['utc_departure'])})

        info_data.update(scratch)
        if scratch['stop_over'] == 0:
            message = f"Low price alert! only €{scratch.get('price')} to fly from {scratch.get('cityFrom')}-" \
                      f"{scratch.get('flyFrom')} to {scratch.get('cityTo')}-{scratch.get('flyTo')}, " \
                      f"from {scratch['arrival_tz']} to {scratch['departure_tz']}." \
                      f"link = https://www.google.co.uk/flights?hl=en#flt=STN.SXF.2020-08-25*SXF.STN.2020-09-08"
            return message
        elif scratch['stop_over'] == 1:
            message = f"Low price alert! only €{scratch.get('price')} to fly from {scratch.get('cityFrom')}-" \
                      f"{scratch.get('flyFrom')} to {scratch.get('cityTo')}-{scratch.get('flyTo')}, " \
                      f"from {scratch['arrival_tz']} to {scratch['departure_tz']}.\n\n" \
                      f"Flight has {scratch['stop_over']} stop, via {scratch['via_city']}."
            return message

    def change_date_format(self, date_string):
        source_data = datetime.datetime.strptime(date_string[:-5], "%Y-%m-%dT%H:%M:%S")
        current_tz = pytz.UTC
        current_date = current_tz.localize(source_data)
        new_TZ = pytz.timezone("Asia/Kolkata")
        new_date = current_date.astimezone(new_TZ)
        new_date_str = new_date.strftime("%Y-%m-%d")
        # print(new_date_str)
        return new_date_str




