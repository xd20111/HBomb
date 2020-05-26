#!/usr/bin/env python
from datetime import datetime
import os
import hashlib
import sys
import time
import threading
import string
import random
import base64
import urllib.request
import urllib.parse
import subprocess
import webbrowser
import smtplib
import sys
import os
import subprocess

Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'
verl = open(".version", 'r').read()



def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def banner():
    
    clr()
    logo="""
 ██░ ██  ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   
▓██░ ██▒▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ 
▒██▀▀██░▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██
░▓█ ░██ ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  
░▓█▒░██▓░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓
 ▒ ░░▒░▒░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒
 ▒ ░▒░ ░▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░ 
 ░  ░░ ░ ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░ 
 ░  ░  ░ ░          ░ ░         ░    ░      
              ░                           ░
               ""","""
----------------   ----------------------
| KLS  Project |   | Version : """,verl,""" |
----------------   ----------------------
\n\tCreated by Honey Pots...\n
-------------------------------------------- 
"""
    print(Red+logo[0]+Blue+logo[1]+logo[2]+logo[3])


def mail():
    RG = str(input("Enter Victim Mail address : "))
    num = input("Enter Number of Mail : ")
    while num == '':
        num = input("Please Enter Number of Mail : ")

    while num.isdigit() != True:
        num = input("\aInvalid! Please Enter Number of Mail : ")

    mail = int(num) + 1
    print("\n\t\t Please Wait Bombing Start...")
    while True:
        try:
          for a in range(1, int(mail)) :
            URL = ""
            r = requests.get(url = URL, params = PARAMS)
            pastebin_url = r.text 
            print("The pastebin URL is:%s"%pastebin_url) 
            clr()
            banner()
            print(Blue)
            print("-------------------------------------------- ")
            print(Red +"                  Details "+Blue)
            print(" Target Mail             : ",RG)
            print(" Number of Requests Sent : ",num)
            print(" Successful Requests     : ",int(a))
            print(" Failed Requests         : ",0)
            print("-------------------------------------------- ")
            print("            Bombing In Progress")
          clr()
          banner() 
          print(str(num) + " Mail Send Successful To  " + str(RG))
          input("\n\nPress Enter To Run Again HBomb Tool : ")  
          subprocess.call([sys.executable, 'HBomb.py']) 
        except :
            print("Victim mail not correct !!!")
            RG = str(input("Enter Victim Mail address : "))
            print("\n\t\t Please Wait Bombing Start...")
            continue         
        pass
clr()
banner()
try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("   You are not connected To Internet!!!")
    print("\n  Please Connect To Internet To Continue...\n")
    input('   Press Enter To Use Again Mail Bombing ...')
    subprocess.call([sys.executable, 'ml.py'])
mail()
