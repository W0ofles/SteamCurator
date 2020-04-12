import steam.steamid
import requests as r
import json
from bs4 import BeautifulSoup
from selenium import webdriver

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





driver = webdriver.Firefox()
driver.get('https://store.steampowered.com/app/727020/Arcade_Moonlander_Plus/')
test_web = driver.find_element_by_class_name("btn_addtocart").click()


page = requests.get("https://isthereanydeal.com/#/")
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(class_="cntBoxContent")
sales = table.find_all(class_="bundle-container-outer bundle-preview giveaway")
#bundles = table.find_all(class_="bundle-container-outer bundle-preview bundle")
links = table.find_all(class_="lg")


test = []
for i in links:
    test.append(i.get('href'))

str_list = (filter(None, test))
str_list = list(set(str_list))

for i in str_list:
    print(i)
