import languages

import sys
import os
import time
import signal
from time import sleep
from sys import argv
from platform import system
from terminaltables import AsciiTable

#---- standart başlangıç dili İngilizce
mainmenu1, mainmenu2,mainmenu3,help,repomenu,repomenu2,repomenu3,repomenu4,language_desc, language_desc2,updating,options,returnmenu,removed,tools,steg,database,explo,fronc,hardw,infogath,passw,pexploit,rep,reveng,social,top10,vulnreb,winres,wireless,ex,download,downoaltool,note,succ = languages.en()
lng = 'en'
#-----

#--- Dil değiştirme Fonksiyonu 
def language_change():
    global mainmenu1, mainmenu2,mainmenu3,help,repomenu,repomenu2,repomenu3,repomenu4,language_desc, language_desc2,updating,options,returnmenu,removed,tools,steg,database,explo,fronc,hardw,infogath,passw,pexploit,rep,reveng,social,top10,vulnreb,winres,wireless,ex,download,downoaltool,note,succ, lng
    if lng == 'tr':
        mainmenu1, mainmenu2,mainmenu3,help,repomenu,repomenu2,repomenu3,repomenu4,language_desc, language_desc2,updating,options,returnmenu,removed,tools,steg,database,explo,fronc,hardw,infogath,passw,pexploit,rep,reveng,social,top10,vulnreb,winres,wireless,ex,download,downoaltool,note,succ = languages.en()
        lng = 'en'
    elif lng == 'en':
        mainmenu1, mainmenu2,mainmenu3,help,repomenu,repomenu2,repomenu3,repomenu4,language_desc, language_desc2,updating,options,returnmenu,removed,tools,steg,database,explo,fronc,hardw,infogath,passw,pexploit,rep,reveng,social,top10,vulnreb,winres,wireless,ex,download,downoaltool,note,succ = languages.tr()
        lng = 'tr'
#--- Dil değiştirme Fonksiyonu Son


def sigint_handler(signum, frame):
    os.system("clear")
    print ("CTRL+C detected!")
    print(" \033[1;91m@bye :(\033[1;m")
    sys.exit() 
 
signal.signal(signal.SIGINT, sigint_handler)



def logo():
    print("""    
                )          (          
        ( /(   *   )  )\ )       
        )\())` )  /( (()/(       
        |((_)\  ( )(_)| /(_))  (   
        |_ ((_)(_(_()))(_))_   )\  
        | |/ / |_   _((_)   \ ((_) 
        |   <    | |/ _ \ |) / _ \ 
        |_|\_\   |_|\___/___/\___/@kernelblog                       
        Emre Yılmaz (delosemre) - emreylmz.com   
    """)

def logo2():
        print("""    
                            )          (          
                    ( /(   *   )  )\ )       
                    )\())` )  /( (()/(       
                    |((_)\  ( )(_)| /(_))  (   
                    |_ ((_)(_(_()))(_))_   )\  
                    | |/ / |_   _((_)   \ ((_) 
                    |   <    | |/ _ \ |) / _ \ 
                    |_|\_\   |_|\___/___/\___/@kernelblog                       
                    Emre Yılmaz (delosemre) - emreylmz.com   
    """)


def mainmenu():
    os.system("clear")
    logo()
    print(f"""
        1) {mainmenu1}
        2) {mainmenu2}
        3) {mainmenu3}
        4) {help}
        5) {ex}

    """)

def downloadtoolmenu():

    table = (
                (f"1- 802.11 {tools}",f"14- {reveng} {tools}"),
                (f"2- bluetooth {tools}",f"15- RFID {tools}"),
                (f"3- {steg} {tools}",f"16- SDR {tools}"),
                (f"4- {database} {tools}",f"17- sniffing & spoofing {tools}"),
                (f"5- {explo} {tools}",f"18- {social} {tools}"),
                (f"6- {fronc} {tools}",f"19- {top10}"),
                (f"7- Fuzzing {tools}",f"20- {social} {tools}"),
                (f"8- GPU {tools}",f"21- {social} {tools}"),
                (f"9- {hardw} {tools}",f"22- Web {tools}"),
                (f"10- {infogath} {tools}",f"23- {winres} {tools}"),
                (f"11- {passw} {tools}",f"24- {wireless} {tools}"),
                (f"12- {pexploit} {tools}",f"25- {repomenu4}"),
                (f"13- {rep} {tools}",f"26- {ex}")
                )
    baslik="Emre Yılmaz @delosemre"
    table_instance = AsciiTable(table, baslik)
    table_instance.inner_heading_row_border = False
    print(downoaltool)
    print(" ")
    print(table_instance.table)
    print()





def baslangic():
    mainmenu()
    print(f"{options}")
    secim = input("root""\033[1;91m@emreylmzcom:~$\033[1;m ")
    if secim == "1":
        os.system("clear")
        logo()
        print(f"""
        1) {repomenu}
        2) {repomenu2}
        3) {repomenu3}
        4) {repomenu4}
            
        
        """)
        print(options)
        secim1 = input("root""\033[1;91m@emreylmzcom:~$\033[1;m ")
        if secim1=="1":
            os.system("sudo cp source/kali-archive-keyring.gpg /etc/apt/trusted.gpg.d/")
            os.system("echo '# Kali linux | KToDo\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list.d/ktodo.list")
            os.system("sudo apt update")
            print(succ)
            print(returnmenu)
            time.sleep(2.5)
            baslangic()
        
        if secim1=="2":
            print(updating)
            os.system("sudo apt update")
            print(returnmenu)
            baslangic()

        if secim1=="3":
            os.system("sudo rm -rf /etc/apt/sources.list.d/ktodo.list")
            os.system("sudo rm -rf /etc/apt/trusted.gpg.d/kali-archive-keyring.gpg")
            
            print(removed)
            print(returnmenu)
            time.sleep(2.5)
            baslangic()

        if secim1=="4":
            print(repomenu)
            baslangic()

    
    if secim=="2":
        # Araç Kaynak | Tools Source
        # https://www.kali.org/tools/kali-meta/
        # https://www.kali.org/docs/general-use/metapackages/
        def toolsdownload():
            os.system("clear")
            logo2()
            downloadtoolmenu()

            print(options)
            secimtools=input("root""\033[1;91m@emreylmzcom:~$\033[1;m ")
            if secimtools=="1":
                print(download)
                os.system("sudo apt install kali-tools-802-11")
                toolsdownload()
            if secimtools=="2":
                print(download)
                os.system("sudo apt install kali-tools-bluetooth")
                toolsdownload()
            if secimtools=="3":
                print(download)
                os.system("sudo apt install kali-tools-crypto-stego")
                toolsdownload()
            if secimtools=="4":
                print(download)
                os.system("sudo apt install kali-tools-database")
                toolsdownload()
            if secimtools=="5":
                print(download)
                os.system("sudo apt install kali-tools-exploitation")
                toolsdownload()
            if secimtools=="6":
                print(download)
                os.system("sudo apt install kali-tools-forensics")
                toolsdownload()
            if secimtools=="7":
                print(download)
                os.system("sudo apt install kali-tools-fuzzing")
                toolsdownload()
            if secimtools=="8":
                print(download)
                os.system("sudo apt install kali-tools-gpu")
                toolsdownload()
            if secimtools=="9":
                print(download)
                os.system("sudo apt install kali-tools-hardware")
                toolsdownload()
            if secimtools=="10":
                print(download)
                os.system("sudo apt install kali-tools-information-gathering")
                toolsdownload()
            if secimtools=="11":
                print(download)
                os.system("sudo apt install kali-tools-passwords")
                toolsdownload()
            if secimtools=="12":
                print(download)
                os.system("sudo apt install kali-tools-post-exploitation")
                toolsdownload()
            if secimtools=="13":
                print(download)
                os.system("sudo apt install kali-tools-reporting")
                toolsdownload()
            if secimtools=="14":
                print(download)
                os.system("sudo apt install kali-tools-reverse-engineering")
                toolsdownload()
            if secimtools=="15":
                print(download)
                os.system("sudo apt install install kali-tools-rfid")
                toolsdownload()
            if secimtools=="16":
                print(download)
                os.system("sudo apt install kali-tools-sdr")
                toolsdownload()
            if secimtools=="17":
                print(download)
                os.system("sudo apt install kali-tools-sniffing-spoofing")
                toolsdownload()
            if secimtools=="18":
                print(download)
                os.system("sudo apt install kali-tools-social-engineering")
                toolsdownload()
            if secimtools=="19":
                print(download)
                os.system("sudo apt install kali-tools-top10")
                toolsdownload()
            if secimtools=="20":
                print(download)
                os.system("sudo apt install kali-tools-voip")
                toolsdownload()
            if secimtools=="21":
                print(download)
                os.system("sudo apt install kali-tools-vulnerability")
                toolsdownload()
            if secimtools=="22":
                print(download)
                os.system("sudo apt install kali-tools-web")
                toolsdownload()
            if secimtools=="23":
                print(download)
                os.system("sudo apt install kali-tools-windows-resources")
                toolsdownload()
            if secimtools=="24":
                print(download)
                os.system("sudo apt install kali-tools-wireless")
                toolsdownload()
            if secimtools=="25":
                os.system("clear")
                baslangic()
            if secimtools=="26":
                os.system("clear")
                print(" \033[1;91m@bye <3\033[1;m")
                os.system("exit")
            else:
                os.system("clear")
                print(options)
                print(returnmenu)
                time.sleep(0.5)
                toolsdownload()

        toolsdownload()




    if secim=="3":
        data = input(language_desc)
        if data == 'y' or data == 'Y' or data == 'e' or data == 'E':
            language_change()
            print(language_desc2)
            baslangic()
        else:
            baslangic()
    
    if secim=="4":
        print(f"""

{note}


            Github: https://github.com/delosemre
            Website: https://emreylmz.com | https://kernelblog.org
            Twitter: https://twitter.com/delosemre

            1) {repomenu4}
            2) {ex}
        """)
        secim4=input("root""\033[1;91m@emreylmzcom:~$\033[1;m ")
        if secim4 == "1":
            baslangic()
        if secim4 == "2":
            os.system("clear")
            print(" \033[1;91m@bye <3\033[1;m")
            os.system("exit")
        else:
            os.system("clear")
            baslangic()

    

    if secim=="5":
        os.system("clear")
        print(" \033[1;91m@bye <3\033[1;m")
        os.system("exit")

    else:
        print(options)
        print(returnmenu)
        time.sleep(0.5)
        baslangic()



# Root Kontrol
def rootkontrol():
    if os.geteuid()==0:
        baslangic()
    else:
        print("root ile çalıştırın! | run with root!")
        sys.exit()

rootkontrol()