import steam.webauth as wa
import time
import requests
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

window = tk.Tk()
window.title("SteamCurator")
window.geometry('700x400')
UserFont = 'Arial Bold'

def login_clicked():
    #lbl_verbose.configure(text="Starting...")
    #lbl_verbose.configure(text="Opening Windows")
    btn_login.configure(text="Logging in...")
    options = Options()
    if HeadlessModeEnabled.get() == 1:
        options.add_argument('--headless')
    else:
        pass
    driver = webdriver.Firefox(options=options)
    username = txt_username.get()
    password = txt_password.get()
    mfa = txt_2fa.get()
    user = wa.WebAuth(username, password)
    session = user.login(twofactor_code=mfa)
    session.get('https://steamcommunity.com')
    def DoTheSoup():
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
        if SteamLinksOnly.get() == 1:
            for i in str_list:
                if "steampowered" in i:
                    links_list.append(i)
                    print("Opening Links From Steam Only -->:", i)
        else:
            for i in str_list:
                links_list.append(i)
                print("Opening All Links -->:", i)
        return links_list
    def SteamAccess(gameLink):
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
    for i in DoTheSoup():
        SteamAccess(i)
    btn_login.configure(text="Done!", bg="green")
    #lbl_verbose.configure(text="^w^")

def exit_clicked():
    quit()

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

class WatchDoge:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.label = tk.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = ttk.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = ttk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")


#
login_window = WatchDoge(window)
#
lbl_username = tk.Label(window, text="Username:", font=(UserFont, 30))
lbl_username.pack()
txt_username = tk.Entry(window,width=30)
txt_username.pack()
lbl_password = tk.Label(window, text="Password:", font=(UserFont, 30))
lbl_password.pack()
txt_password = tk.Entry(window,width=30)
txt_password.pack()
lbl_2fa = tk.Label(window, text="Auth Code:", font=(UserFont, 30))
lbl_2fa.pack()
txt_2fa = tk.Entry(window,width=10)
txt_2fa.pack()
SteamLinksOnly = tk.IntVar()
HeadlessModeEnabled = tk.IntVar()
checkBox1 = tk.Checkbutton(window, variable=SteamLinksOnly, onvalue=1, offvalue=0, text="Only Open Steam Links")
checkBox2 = tk.Checkbutton(window, variable=HeadlessModeEnabled, onvalue=1, offvalue=0, text="Operate in 'Headless' Mode?")
checkBox1.pack()
checkBox2.pack()
btn_login = tk.Button(window, text="Login", bg="yellow", fg="black", font=(UserFont, 30), command=login_clicked)
btn_login.pack()
btn_exit = ttk.Button(window, text="Exit", command=exit_clicked)
btn_exit.pack()





window.mainloop()



