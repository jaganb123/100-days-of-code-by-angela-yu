# with open("./weather_data.csv") as weather:
#     data_1 = weather.readlines()
#     data = []
#     for i in data_1:
#         data.append(i.strip())
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for i in data:
#         if i[1] == "temp":
#             continue
#         temprature.append(int(i[1]))
#     print(temprature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data.to_dict())
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # temp_avg = sum(temp_list)/len(temp_list)
# # print(round(temp_avg))
# # print(data["temp"].max())
# #
# temp_in_celcius = data[data.day == "Monday"]["temp"]
# temp_in_faranhit = (temp_in_celcius * 9/5) + 32
# print(temp_in_faranhit)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colors = data["Primary Fur Color"].unique()
gray_color_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_color_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_squirrel = len(data[data["Primary Fur Color"] == " Black"])
squirrel_count = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_color_squirrel, red_color_squirrel, black_color_squirrel]
}

df = pandas.DataFrame(squirrel_count)
df.to_csv("Squirrel_count.csv")
