import steam.steamid
import requests as r
import json

test = r.get('http://store.steampowered.com/api/appdetails?appids=57690')

output = test.json()
print(str(output['57690']['data']["price_overview"]['final']))





