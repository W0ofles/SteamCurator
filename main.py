import steam.webauth as wa
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm

page = requests.get("https://isthereanydeal.com/#/")
soup = BeautifulSoup(page.content, 'html.parser')

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

username = input("Steam Username: ")
password = input("Steam Password: ")
mfa = input("Steam Authenticator Code: ")

user = wa.WebAuth(username, password)
session = user.login(twofactor_code=mfa)
session.get('https://steamcommunity.com')

table = soup.find(class_="cntBoxContent")
sales = table.find_all(class_="bundle-container-outer bundle-preview giveaway")
#bundles = table.find_all(class_="bundle-container-outer bundle-preview bundle")
links = table.find_all(class_="lg")

tags = []
for i in links:
    tags.append(i.get('href'))

str_list = (filter(None, tags))
str_list = list(set(str_list))

links_list = []
for i in str_list:
    if "steampowered" in i:
        links_list.append(i)
        print("Adding:", i)

def SteamAccess(gameLink):
    driver.get(gameLink)
    for c in session.cookies :
        driver.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})
    driver.get(gameLink)
    driver.add_cookie
    try:
        web = driver.find_element_by_class_name("btn_addtocart").click()
    except:
        pass
    finally:
        driver.quit()
for i in tqdm(links_list):
    SteamAccess(i)