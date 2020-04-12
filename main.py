import steam.steamid
import requests as r
import json

games = r.get('https://api.steampowered.com/ISteamApps/GetAppList/v1')
games_json = games.json()
games_json = (games_json['applist']['apps']['app'])

game_arr = []
counter = 0
for i in range(len(games_json)):
    game_arr.append(games_json[counter]['appid'])
    counter = counter + 1




test = r.get('http://store.steampowered.com/api/appdetails?appids=57690')

output = test.json()
print(str(output['57690']['data']["price_overview"]['final']))

