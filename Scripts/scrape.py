# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pymongo
import json
import pprint

# Google developer API key
# from config import gkey
gkey = 'AIzaSyB-Bq-L4N1L0iOuuGYIEcvsV_loPjf0-TQ'


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


url = 'https://visitseattle.org/things-to-do/sightseeing/top-25-attractions/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


a=soup.find_all('div', class_="medium-7")
attractions = []
for x in a:
    s= x.find('h3').text
    attractions.append(s)
# Close splinter window
browser.quit()


attraction_details = []

# base url
base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

for attraction in attractions:
    # set up a parameters dictionary
    params = {
        "locationbias": "point:47.6062, 122.3321",
        "input": attraction,
        "inputtype":"textquery",
        "key": gkey,
        "fields":"name,geometry"
        }
    # run a request using our params dictionary
    response = requests.get(base_url, params=params)
    # convert response to json
    places_data = response.json()
    print(places_data["candidates"][0]["name"])
    print(places_data["candidates"][0]["geometry"]["location"]['lat'])
    print(places_data["candidates"][0]["geometry"]["location"]['lng'])
    print("------------------")
    attraction_details.append({"name":places_data["candidates"][0]["name"],
                                "lat":places_data["candidates"][0]["geometry"]["location"]['lat'],
                                "lng":places_data["candidates"][0]["geometry"]["location"]['lng']})


df = pd.DataFrame(data=attraction_details)
df.to_csv('../Resources/Attractions.csv', index=False)

