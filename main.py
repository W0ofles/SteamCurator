import requests
from bs4 import BeautifulSoup
page = requests.get("https://isthereanydeal.com/#/")
soup = BeautifulSoup(page.content, 'html.parser')
gamelist = []

for link in soup.find_all('a', class_='lg'): #Find Links
    gamelist.append(link.get('href')) #Get Hrefs
gamelist = list(dict.fromkeys(gamelist)) #Remove Duplicates

print(gamelist)
