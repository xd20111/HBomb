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

Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'
verl = open("/opt/HBomb/.version", 'r').read()


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

\tCreated by Honey Pots...

-------------------------------------------- 

"""
    print(Red+logo[0]+Blue+logo[1]+logo[2]+logo[3])

def home():
	print(Red +"""       [ Main Menu ] \n"""+ Blue + """
[1] Mail Bombing
[2] SMS Bombing 
[3] Call Bombing 
[4] Restart
[5] Help
[6] Exit 
""")

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\tYour Internet Speed is Slow ...")
        print('\t\tTBomb Will Stop Now...\n\n')
        banner()
        exit()


def update():
    stuff_to_update = ['HBomb.py','ml.py','smcl.py', '.version']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen(
            "https://raw.githubusercontent.com/HoneyPots0/HBomb/master/" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()
    print('\n\t    Updated Successfull !!!')
    input('\n\tPress Enter To Run Again HBomb Tool: ')
    subprocess.call([sys.executable, 'HBomb.py'])

clr()
banner()
try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("   You are not connected To Internet!!!")
    print("\n  Please Connect To Internet To Continue...\n")
    input('   Press Enter To Run Again HBomb Tool ...')
    subprocess.call([sys.executable, 'HBomb.py'])

print('\t   Checking For Updates...')
ver = urllib.request.urlopen(
    "https://raw.githubusercontent.com/HoneyPots0/HBomb/master/.version").read().decode('utf-8')
verl = ''
try:
    verl = open("/opt/HBomb/.version", 'r').read()
except Exception:
    pass
if ver != verl:
    print('\n\tNew Version Available : ', ver)
    print('\n\t  HBomb Tool Start Updating...')
    update()
print("\n\tYour Version is Up-To-Date")
print('\n\t     Starting HBomb...\n')
time.sleep(4)

clr()
banner()
home()
bomb = input("Choose one options : ")
while bomb.isdigit() != True:
    bomb = input("\aInvalid ! Choose one options  [ 1 to 6]: ")

while int(bomb) > 6 :
    bomb = input("\aInvalid ! Choose one options  [ 1 to 6]: ")
clr()
banner()
if int(bomb) == 1 : 
    subprocess.call([sys.executable, '/opt/HBomb/ml.py'])
elif int(bomb) == 2 :
	subprocess.call([sys.executable, '/opt/HBomb/smcl.py'])
elif int(bomb) == 3 :
	subprocess.call([sys.executable, '/opt/HBomb/smcl.py', 'call'])
elif int(bomb) == 4 :
    subprocess.call([sys.executable, '/opt/HBomb/HBomb.py'])

elif int(bomb) == 5 :
        webbrowser.open('https://honey0pots.000webhostapp.com/KLS/HBomb/', new=2)
        print("If You Use Mobile . May be Website not open automatically \n Visit : https://honey0pots.000webhostapp.com/KLS/HBomb/")
        input("\nPress Enter To Run HBomb Tool Again : ")
        subprocess.call([sys.executable, 'HBomb.py'])

elif int(bomb) == 6:
    print("\tThank you for using ... Byee \n\n")
    exit()
else :
    home()
    bomb = input("\aInvalid ! Choose one options  [ 1 to 6]: ")
    clr()
    banner()
    if int(bomb) == 1 : 
        subprocess.call([sys.executable, '/opt/HBomb/ml.py'])
    elif int(bomb) == 2 :
        subprocess.call([sys.executable, '/opt/HBomb/smcl.py'])
    elif int(bomb) == 3 :
        subprocess.call([sys.executable, '/opt/HBomb/smcl.py', 'call'])
    elif int(bomb) == 4 :
        subprocess.call([sys.executable, '/opt/HBomb/HBomb.py'])

    elif int(bomb) == 5 :
            webbrowser.open('https://honey0pots.000webhostapp.com/KLS/HBomb/', new=2)
            print("If You Use Mobile . May be Website not open automatically \n Visit : https://honey0pots.000webhostapp.com/KLS/HBomb/")
            input("\nPress Enter To Run HBomb Tool Again : ")
            subprocess.call([sys.executable, '/opt/HBomb/HBomb.py'])

    elif int(bomb) == 6:
        print("\tThank you for using ... Byee \n\n")
        exit()
    else :
        home()
        bomb = input("\aInvalid ! Choose one options  [ 1 to 6]: ")

