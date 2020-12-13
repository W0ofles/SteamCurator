import steam.webauth as wa
import time
import threading
import requests
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def startsession(user,mfa):
    global session
    session = user.login(twofactor_code=mfa)
    session.get('https://steamcommunity.com')
    return session

def DoTheSoup(username,password,mfa,SteamLinksOnly,options):
    driver = webdriver.Firefox(options=options)
    user = wa.WebAuth(username, password)
    startsession(user,mfa)
    page = requests.get("https://isthereanydeal.com/#/")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find(class_="cntBoxContent")
    links = table.find_all(class_="lg")
    tags = []
    for i in links:
        tags.append(i.get('href'))
    str_list = (filter(None, tags))
    str_list = list(set(str_list))
    links_list = []
    if SteamLinksOnly == 1:
        for i in str_list:
            if "steampowered" in i:
                links_list.append(i)
                print("Opening Links From Steam Only -->:", i)
    else:
        for i in str_list:
            links_list.append(i)
            print("Opening All Links -->:", i)
    return links_list





def SteamAccess(gameLink,options):
    driver = webdriver.Firefox(options=options)
    driver.get(gameLink)
    for c in session.cookies :
        driver.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})
    driver.get(gameLink) #Fix?
    #driver.add_cookie()
    #FIXME: add_cookie() brings up error. Was this planned?
    try:
        web = driver.find_element_by_class_name("btn_addtocart").click()
    except:
        pass
    finally:
        driver.quit()