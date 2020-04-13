import steam.webauth as wa
import requests
from tkinter import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

window = Tk()
window.title("SteamCurator")
window.geometry('700x400')

lbl_username = Label(window, text="Username:", font=("Arial Bold", 30))
lbl_username.grid(column=0, row=3)
txt_username = Entry(window,width=30)
txt_username.grid(column=1, row=3)
lbl_password = Label(window, text="Password:", font=("Arial Bold", 30))
lbl_password.grid(column=0, row=4)
txt_password = Entry(window,width=30)
txt_password.grid(column=1, row=4)
lbl_2fa = Label(window, text="Auth Code:", font=("Arial Bold", 30))
lbl_2fa.grid(column=0, row=5)
txt_2fa = Entry(window,width=10)
txt_2fa.grid(column=1, row=5)
lbl_verbose = Label(window, text="CONSOLE", font=("Arial Bold", 30), fg='white', bg='black')
lbl_verbose.grid(column=1, row=7)


def login_clicked():
    btn_login.configure(text="Logging in...")
    lbl_verbose.configure(text="Starting...")
    options = Options()
    options.add_argument('--headless')
    username = txt_username.get()
    password = txt_password.get()
    mfa = txt_2fa.get()
    user = wa.WebAuth(username, password)
    session = user.login(twofactor_code=mfa)
    session.get('https://steamcommunity.com')
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
    for i in str_list:
        links_list.append(i)
    def SteamAccess(gameLink):
        driver = webdriver.Firefox(options=options)
        driver.get(gameLink)
        for c in session.cookies :
            driver.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})
        driver.get(gameLink) #Fix?
        driver.add_cookie
        try:
            web = driver.find_element_by_class_name("btn_addtocart").click()
        except:
            pass
        finally:
            driver.quit()
    lbl_verbose.configure(text="Sending Requests...")
    for i in links_list:
        SteamAccess(i)
    btn_login.configure(text="Done!", bg="green")

def exit_clicked():
    quit()


btn_login = Button(window, text="Login", bg="yellow", fg="black", font=("Arial Bold", 30), command=login_clicked)
btn_login.grid(column=1, row=6)
btn_exit = Button(window, text="Exit", bg="red", fg="black", font=("Arial Bold", 15), command=exit_clicked)
btn_exit.grid(column=2, row=6)


if __name__ == '__main__':
    window.mainloop()



