import steam.webauth as wa
import time
import threading
import requests
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from souplogic import DoTheSoup
from souplogic import SteamAccess

#TODO: Add a database to store username and password.

class MainTitle:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        UserFont = 'Arial Bold'
        #TODO: Make UI Look Prettier.
        self.lbl_username = tk.Label(self.frame, text="Username:", font=(UserFont, 30))
        self.lbl_username.pack()
        self.txt_username = tk.Entry(self.frame,width=30)
        self.txt_username.pack()
        self.lbl_password = tk.Label(self.frame, text="Password:", font=(UserFont, 30))
        self.lbl_password.pack()
        self.txt_password = tk.Entry(self.frame,width=30)
        self.txt_password.pack()
        self.lbl_2fa = tk.Label(self.frame, text="Auth Code:", font=(UserFont, 30))
        self.lbl_2fa.pack()
        self.txt_2fa = tk.Entry(self.frame,width=10)
        self.txt_2fa.pack()
        self.SteamLinksOnly = tk.IntVar()
        self.HeadlessModeEnabled = tk.IntVar()
        self.checkBox1 = tk.Checkbutton(self.frame, variable=self.SteamLinksOnly, onvalue=1, offvalue=0, text="Only Open Steam Links")
        self.checkBox2 = tk.Checkbutton(self.frame, variable=self.HeadlessModeEnabled, onvalue=1, offvalue=0, text="Operate in 'Headless' Mode?")
        self.checkBox1.pack()
        self.checkBox2.pack()
        self.btn_login = tk.Button(self.frame, text="Login", bg="yellow", fg="black", font=(UserFont, 30), command=self.login_clicked)
        self.btn_login.pack()
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.btn_exit = ttk.Button(self.frame, text="Exit", command=self.exit_clicked)
        self.btn_exit.pack()
        self.frame.pack()

    def login_clicked(self):
        username = self.txt_username.get()
        password = self.txt_password.get()
        mfa = self.txt_2fa.get()
        HeadlessModeEnabled = self.HeadlessModeEnabled.get()
        SteamLinksOnly = self.SteamLinksOnly.get()
        options = Options()
        if HeadlessModeEnabled == 1:
            options.add_argument('--headless')
        else:
            pass
        DoTheSoup(username,password,mfa,SteamLinksOnly,options)
        #TODO: Thread Processes of application so mainloop doesn't freeze constantly.
        #xthread = threading.Thread(target=DoTheSoup)
        #xthread.start()
        #xthread.join()
        #ythread = threading.Thread(target=SteamAccess, args=(1,))
        #ythread.start()
        for i in DoTheSoup(username,password,mfa,SteamLinksOnly,options):
            SteamAccess(i,options)
            return
    #TODO: Add Secondary window.
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
    def exit_clicked(self):
        quit()

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main():
    window = tk.Tk()
    app = MainTitle(window)
    window.title("SteamCurator")
    window.geometry('700x400')
    window.mainloop()

if __name__ == '__main__':
    main()


