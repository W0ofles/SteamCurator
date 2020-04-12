import requests
from bs4 import BeautifulSoup
list = []

page = requests.get("https://isthereanydeal.com/#/")
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(class_="cntBoxContent")
sales = table.find_all(class_="bundle-container-outer bundle-preview giveaway")
bundles = table.find_all(class_="bundle-container-outer bundle-preview bundle")
links = table.find_all(class_="lg")

print(soup.find_all('a', class_='lg'))