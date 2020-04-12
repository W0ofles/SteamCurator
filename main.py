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



for i in game_arr:
    try:
        game_query = r.get('http://store.steampowered.com/api/appdetails?appids=' + str(i))
        game_query = game_query.json()
        print(game_query[str(i)]['data']["price_overview"]['final'])
    except:
        print('no price')
