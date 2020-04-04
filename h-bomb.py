#!/usr/bin/env python
import os
import sys
import os
import subprocess

Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\tYour Internet Speed is Slow or You Are Using Proxies...")
        print('\t\tHBomb Will Stop Now...\n\n')
        banner()
        exit()
        
def update():
    stuff_to_update = ['HBomb.py', '.version']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen(
            "" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()
    print('\n\t\tUpdated Successfull !!!!')
    print('\tPlease Run The Script Again...')
    exit()

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
----------------   --------------------
| KLS  Project |   | Version : 2020.4 |
----------------   --------------------

\tCreated by Honey Pots...

-------------------------------------------- 

"""
    print(Red+logo[0]+Blue+logo[1])

def home():
	print(Red +"""       [ Main Menu ] \n"""+ Blue + """
[1] Mail Bombing
[2] SMS Bombing 
[3] Call Bombing 
[4] Telegram Massage Bombing
[5] Help
[6] Exit 
""")

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
    subprocess.call([sys.executable, 'ml.py'])
elif int(bomb) == 2 :
	subprocess.call([sys.executable, 'smcl.py'])
elif int(bomb) == 3 :
	subprocess.call([sys.executable, 'smcl.py', 'call'])
elif int(bomb) == 4 :
	print("Sorry this feature not available now 4 ")
elif int(bomb) == 5 :
	print("sorry this feature not available now 5")
elif int(bomb) == 6:
    print("\tThank you for using ... Byee \n\n")
    exit()
else :
    print("Invalid!")


