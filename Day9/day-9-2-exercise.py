travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

def AddNewCountry(CountryName, NoOfVisit, Cities):
    travel_log.append({"country": CountryName, "visits": NoOfVisit, "cities": Cities})


AddNewCountry(CountryName="USA", NoOfVisit=1, Cities=["Washington D.C.", "New York", "Los Angels"])
print(travel_log)
