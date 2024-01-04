import random
import time
import colorama
import shutil
from pystyle import Center,Colors,Colorate
import pystyle
from colorama import Fore, Back, Style
import os
import sys
colorama.init()
culur = Colors.red_to_purple
culour = pystyle.Colors.black_to_red
def clear_screen():
    print("\n" * 50)

logo = """
 .d8888b.              
d88P  Y88b          
888    888          
888    888 888  888 
888    888 `Y8bd8P' 
888    888   X88K    - BETA -
Y88b  d88P .d8""8b. 
 "Y8888P"  888  888 

"""
##database
import subprocess
from github import Github
import base64
import json
import time
__ALREADY__ = False
HWID = str(subprocess.check_output("wmic csproduct get uuid"), "utf-8").split("\n")[1].strip()
_ = "_"
p = "h"
h = "g"
full = "private."
culur = Colors.yellow_to_red
##database
def add_data_to_base():
    global UID , __ALREADY__
    addon = 0
    g = Github(f"{h}{p}p{_}{base64.b64decode(full).decode()}")
    repo = g.get_repo("144-lines/private-database")
    contents = repo.get_contents("")
    for file in contents:
        correct_file = str(file).replace("ContentFile(path=","").replace(")","").replace('"',"")
        if HWID in correct_file:
            UID = str(correct_file).replace("int144","").replace(".json","").replace("_","").replace(HWID,"").replace("UID=","")
            __ALREADY__ = True
        elif "int144_" in correct_file and HWID not in correct_file:
            addon += 1
    if __ALREADY__ == False:
        json_dat={'u': '', 'p': ''}
        try:
            repo.create_file(f'int144_UID={addon}_{HWID}.json', f'data file for uid {addon}',f"{json_dat}")
            UID = addon
        except:
            pass
add_data_to_base()
NAME_ = ""
def LOGIN_():
    global NAME_,n
    os.system("cls")
    functions = f'''
[> Please login with your 0x account <]

         .d8888b.              
        d88P  Y88b          
        888    888          
        888    888 888  888 
        888    888 `Y8bd8P' 
        888    888   X88K   
        Y88b  d88P .d8""8b. 
         "Y8888P"  888  888 

===========================================
                       '''
    print(Colorate.Horizontal(culur, Center.XCenter(functions)))
    user_ = input(Colorate.Horizontal(culur, f"[>] Username: "))
    pass_ = input(Colorate.Horizontal(culur, f"[>] Password: "))
    g = Github(f"{h}{p}p{_}{base64.b64decode(full).decode()}")
    repo = g.get_repo("144-lines/private-database")
    contents = repo.get_contents("")
    for file in contents:
        correct_file = str(file).replace("ContentFile(path=", "").replace(")", "").replace('"', "")
        if HWID in correct_file:
            raw = repo.get_contents(correct_file).decoded_content.decode().replace("'",'"')
            json_info = json.loads(raw)
            us = json_info.get("u")
            pa = json_info.get("p")
            if user_ == us:
                if pass_ == pa:
                    NAME_ = us
                else:
                    print("Wrong Password or Username")
                    time.sleep(5)
                    os._exit(0)
            else:
                print("Wrong Password or Username")
                time.sleep(5)
                os._exit(0)
LOGIN_()
clear_screen()
banner1 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   

                                  .d8888b.              
                                 d88P  Y88b          
                                 888    888           
                                 888    888 888  888  
                                 888    888 `Y8bd8P'  
                                 888    888   X88K    official 0x Product
                                 Y88b  d88P .d8""8b.   By .gekkefries
                                  "Y8888P"  888  888 
          
                                           ! PRESS ENTER !
                            ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
                            ┇      Made in 2023                                  ┇
                            ┇      [Creator Discord] .gekkefries                 ┇
                            ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
pystyle.Anime.Fade(Center.Center(banner1), culour, Colorate.Horizontal, enter=True)
print(Colorate.Horizontal(culour, Center.XCenter(banner1)))

menu_banner = """
╭━━━━━━━━━━━━━━━━━━━━━━━━╮
┇      [1] >> Start      ┇
┇      [2] >> Exit       ┇
╰━━━━━━━━━━━━━━━━━━━━━━━━╯


"""
print(Colorate.Horizontal(culur, Center.XCenter(menu_banner)))

user_choice = input(Colorate.Horizontal(culur, f"[>>] Selection: "))

if user_choice == '1':
    print(Colorate.Horizontal(Colors.blue_to_purple, f"[!] >> Alright here we go!"))
    clear_screen()

elif user_choice == '2':
    clear_screen()
    print(Colorate.Horizontal(Colors.blue_to_purple, f"[!] >> Closing in 3 seconds..."))
    time.sleep(3)
    print("Script closed.")
    exit()

else:
    print(Colorate.Horizontal(Colors.blue_to_purple, f"[!] >> Invalid Choice. Please choose between 1/2"))
    input(Colorate.Horizontal(culur, f"[!] >> Press enter to exit."))
    exit()

class validator():

    def __init__(self):
        self.cardNumber = None
        self.Brand = None

    def __findBrand(self):
        if self.cardNumber[:2] in ['34', '37']:
            self.Brand = 'American Express'
        elif self.cardNumber[:3] in ['300', '301', '302', '303', '304', '305']:
            self.Brand = 'Diners Club - Carte Blanche'
        elif self.cardNumber[:2] in ['36']:
            self.Brand = 'Diners Club - International'
        elif self.cardNumber[:2] in ['54']:
            self.Brand = 'Diners Club - USA & Canada'
        elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648',
                                                                         '649'] or self.cardNumber[0:2] in [
            '65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif self.cardNumber[:3] in ['637', '638', '639']:
            self.Brand = 'InstaPayment'
        elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
            self.Brand = 'Maestro'
        elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in
                                                                                              range(222100, 272100)]:
            self.Brand = 'MasterCard'
        elif self.cardNumber[:4] in ['4026', '4508', '4844', '4913', '4917'] or self.cardNumber[:6] == '417500':
            self.Brand = 'VISA Electron'
        elif self.cardNumber[0] in ['4']:
            self.Brand = 'VISA'
        else:
            self.Brand = 'Unknown Brand'

    def validate(self, number, amount_choice):
        """
        number: str or int credit card number
        amount_choice: int selected amount choice
        """
        self.cardNumber = str(number)
        lastDigit = int(self.cardNumber[-1])
        base = [int(x) for x in reversed(self.cardNumber[:-1])]
        base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
        base = [x if x <= 9 else x - 9 for x in base]
        base = sum(base)

        if base % 10 == 0 and lastDigit == 0:
            lastDigit = 0
        else:
            lastDigit = 10 - (base % 10)

        if lastDigit == int(self.cardNumber[-1]):
            print(Fore.GREEN)
            file_name = f"{amount_choice}.txt"
            with open(file_name, "a") as file:
                file.write(self.cardNumber + '\n') 
            return f'[!] >> {self.cardNumber} Valid'
        else:
            print(Fore.RED)
            return f'[!] >> {self.cardNumber} Invalid'


options = """

      .d8888b.              
     d88P  Y88b          
     888    888          
     888    888 888  888 
     888    888 `Y8bd8P' 
     888    888   X88K   
     Y88b  d88P .d8""8b. 
      "Y8888P"  888  888 

 ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
 ┇ Please select the amount you want ┇     
 ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
 
 ╭━━━━━━━━━━━━━━━━━━━━━━━━━━╮  
 ┇ [1] >> $1000             ┇ 
 ┇ [2] >> $2000             ┇ 
 ┇ [3] >> $5000             ┇ 
 ┇ [4] >> $7000             ┇ 
 ┇ [5] >> $10.000           ┇ 
 ┇ [6] >> $20.000           ┇
 ┇ [7] >> $40.000           ┇ 
 ┇ [8] >> $100.000          ┇  
 ╰━━━━━━━━━━━━━━━━━━━━━━━━━━╯    
"""
print(Colorate.Horizontal(culur, Center.XCenter(options)))

whatcard = input(Colorate.Horizontal(culur, f"[>>] Selection: "))
print(" ")
print(" ")
whatcard = int(whatcard)
randomnums = "0123456789"

if whatcard == 1:
    howmany = input(Colorate.Horizontal(culur, f"[>>] How many cards?: "))
    time.sleep(0.8)
    print("[/] Please wait... ")
    time.sleep(0.8)
    howmany = int(howmany)

    for x in range(howmany):
        bin = "60457811427"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc), whatcard))





if whatcard == 2:
    howmany = input(Colorate.Horizontal(culur, f"[>>] How many cards?: "))
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578112"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(validator().validate(int(cc),whatcard))

if whatcard == 3:
    howmany = input(Colorate.Horizontal(culur, f"[>>] How many cards?: "))
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578116"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(validator().validate(int(cc),whatcard))

if whatcard == 4:
    howmany = input(Colorate.Horizontal(culur, f"[>>] How many cards?: "))
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578118493"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)
        print(validator().validate(int(cc),whatcard))
if whatcard == 5:
    howmany = input(Colorate.Horizontal(culur, f"[>>] How many cards?: "))
    howmany = int(howmany)
    for x in range(howmany):
        bin = "6045781156"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)
        print(validator().validate(int(cc),whatcard))

if whatcard == 6:
    howmany = input(Colorate.Horizontal(culur, f"[>>] How many cards?: "))
    howmany = int(howmany)
    for x in range(howmany):
        bin = "60457811453"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)
        print(validator().validate(int(cc),whatcard))
		
if whatcard == 7:
    howmany = input(Colorate.Horizontal(culur, f"[>>] How many cards?: "))
    howmany = int(howmany)
    for x in range(howmany):
        bin = "60457811947"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)
        print(validator().validate(int(cc),whatcard))
		
if whatcard == 8:
    howmany = input(Colorate.Horizontal(culur, f"[>>] How many cards?: "))
    howmany = int(howmany)
    for x in range(howmany):
        bin = "60457811859"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)
        print(validator().validate(int(cc),whatcard))
		
        

print(" ")
print(" ")
print(Colorate.Horizontal(Colors.blue_to_purple, f"[!] >> Cards saved."))
print(" ")

input(Colorate.Horizontal(culur, f"Done. Press enter to continue "))

def print_suggester():
    os.system("cls")
    suggester = """
    Credits:

    - By .gekkefries
    ~| Dm me if you have experienced any issues! |~

    ( I'm not responsible for anything that happens. )
    """
    for char in suggester:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)

print_suggester()
input(Colorate.Horizontal(culur, f"[>>] Press enter to exit "))
exit()

