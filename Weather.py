"""
Program: Weather
Author: Joanna Boerner
Last Date Modified:
The purpose of this program is to find the "best" route between five cities
based on the lowest average temperature. The values are retrieved from the openweathermap api.

"""
import requests
import json
from itertools import permutations

API_KEY = "cf752b1a125cc4ddeb6ad0ec9a348ba3"
WS_URL = "https://api.openweathermap.org/data/2.5/forecast?id=524901&units=imperial&APPID="

city_list = []


def retrieve_weather(s):
    hourly_temps = []
    daily_temps = []
    response = requests.get(WS_URL.replace("524901", str(s)) + API_KEY)
    request_url = (WS_URL + API_KEY)
    if response.status_code == 200:
        print(request_url)
        d = json.loads(response.text)

        city_name = (d['city']['name'])

    for items in d['list']:
        if 'main' in items:
            temp = int((items['main']['temp']))
            print(temp)  # here are all the temps we've gathered

        hourly_temps.append(temp)

        if len(hourly_temps) == 8:  # Once we have 8 values, average them to find the temp for that day
            average = sum(hourly_temps) / 8
            print("This is the average: " + str(average))
            # Once you have the daily temp save it to the list of days and move on to the next day
            daily_temps.append(average)
            hourly_temps.clear()  # empty hourly_temps to collect a new set of 8 for the next day

    city_list.append(City(city_name, daily_temps))

    # TEST PRINT ZONE
    """
    for items in hourly_temps:
        print("here are the items contained in hourly_temps: " + str(items))

    for items in daily_temps:
        print("here are the items contained in daily_temps: " + str(items))

    print("sedona")
    for i in range(5):
        print(city_list[0].temps[i])
    """


class City:

    def __init__(self, name, temperatures):
        self.name = name
        self.temps = temperatures

    def get_temperature(self, day):
        return self.temps[day]

    def __str__(self):
        return self.name


class Route:
    def __init__(self, city_list):
        self.city_list = city_list

    def calculate_route(self):

        list = [city_list[0].temps, city_list[1].temps, city_list[2].temps, city_list[3].temps, city_list[4].temps]
        perm = permutations(list)
        lowest_average_temp = 100.00

        for i in perm:

            print(i)  # Dump of all permutations for all cities
            # Pull values from their randomized positions for days 1 - 5
            print(i[0][0], i[1][1], i[2][2], i[3][3], i[4][4], end=" ")
            ave = (i[0][0] + i[1][1] + i[2][2] + i[3][3] + i[4][4])/5  # find the average of each "week" based on values
            print("The sum of these is averaged by 5 is : " + str(ave))
            if ave < lowest_average_temp:  # finding the lowest average
                lowest_average_temp = ave
                iteration_number = i  # saving the iteration to go back and find the city names

        print("The lowest average temp is " + str(lowest_average_temp) + " and is provided by this route: ")

        for i in range(0, 5):
            for j in range(0, 5):
                # find the name of the iteration by comparing it to the original city_list
                if iteration_number[i] == city_list[j].temps:
                    print(str(city_list[j].name), end=", ")


print("S E D O N A")
retrieve_weather(5313667)  # ID for Sedona

print("\nF L A G S T A F F")
retrieve_weather(5294810)  # ID for Flagstaff

print("\nT U S C O N")
retrieve_weather(5318313)  # ID for Tuscon

print("\nP H O E N I X")
retrieve_weather(5308655)  # ID for Phoenix

print("\nL A K E  H A V A S U  C I T Y")
retrieve_weather(5301388)  # ID for Lake Havasu City

Route.calculate_route(city_list)