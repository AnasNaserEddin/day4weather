# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# importing requests and json
import requests, json
# base URL
print("welcome to city checking weather,enter please the city you want to check the weather on it")
BASE_URL = "http://api.weatherapi.com/v1/current.json?"
# City Name
CITY = input()
# API key
API_KEY = "ca906cb4997343508e7165953202010"
# upadting the URL
URL = BASE_URL + "key=" + API_KEY + "&q=" + CITY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
# print(response.status_code)
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['current']
   # getting temperature
   temperature = main['temp_c']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure_in']

   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   # print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("sorry ,enter a valid city name")