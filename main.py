import requests
from bs4 import BeautifulSoup
pricepage = "https://isthereanydeal.com/#/"
page = requests.get(pricepage) #Request The Page
soup = BeautifulSoup(page.content, 'html.parser') #Soup The Page
gamelist = [] #Create Empty List

for link in soup.find_all('a', class_='lg'): #Find Links
    gamelist.append(link.get('href')) #Get Hrefs
gamelist = list(dict.fromkeys(gamelist)) #Remove Duplicates

print(gamelist)