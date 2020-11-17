import random
from random import randint
import time
import sys
import os
gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYNZ123456789'
class colors:

    ENDC     = '\33[0m'
    BOLD     = '\33[1m'
    ITALIC   = '\33[3m'
    URL      = '\33[4m'
    BLINK    = '\33[5m'
    BLINK2   = '\33[6m'
    SELECTED = '\33[7m'

    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'

    GREY    = '\33[90m'
    RED2    = '\33[91m'
    GREEN2  = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2   = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2  = '\33[96m'
    WHITE2  = '\33[97m'

    GREYBG    = '\33[100m'
    REDBG2    = '\33[101m'
    GREENBG2  = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2   = '\33[104m'
    VIOLETBG2 = '\33[105m'   
    BEIGEBG2  = '\33[106m'
    WHITEBG2  = '\33[107m'
print("\33[31m███████╗\33[35m █████╗\33[31m ██╗  ██╗")
print("\33[31m╚══███╔╝\33[35m██╔══██╗\33[31m╚██╗██╔╝")
print("\33[31m  ███╔╝ \33[35m███████║ \33[31m╚███╔╝")
print("\33[31m ███╔╝  \33[35m██╔══██║\33[31m ██╔██╗ ")
print("\33[31m███████╗\33[35m██║  ██║\33[31m██╔╝ ██╗")
print("\33[31m╚══════╝\33[35m╚═╝  ╚═╝\33[31m╚═╝  ╚═╝BETA")
total = input("\33[31mHow Many Codes Do You Need:\33[35m \33[35m")
time.sleep(1.0)
mode = input("\33[31mMinecraft \33[35m~ \33[31mNetflix\n\33[35mXbox \33[31m~ \33[35mPsn \33[31m~ \33[35mRoblox\n\33[31mAmazon \33[35m~ \33[31mEbay\n (BETA SOME DONT WORK)Enter:")
print("processing..")
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
spinner = spinning_cursor()
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
    os.system('clear')
number = int(total)
file = (total+ mode+' ZAXGEN.txt')
file2 = 'ZAXCODEZ.txt'
#Minecraft #minecraft
if(mode == "unkown"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
#netflix #Netflix
if(mode == "umknown"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)
if(mode == "Xbox" or "xbox"):
#Xbox
   if(mode =="xbox"or"Xbox"):
     gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
   for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        space1 = "-"
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        space3 = "-"
        generate16 = random.choice(gentype)
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        generate20 = random.choice(gentype)
        space4 = "-"
        generate21 = random.choice(gentype)
        generate22 = random.choice(gentype)
        generate23 = random.choice(gentype)
        generate24 = random.choice(gentype)
        generate25 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+generate15+space3+generate16+generate17+generate18+generate19+generate20+space4+generate21+generate22+generate23+generate24+generate25+newline)            
if(mode == "Psn"or"psn"):
 gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)
            #roblox #Roblox
        if(mode == "Roblox"or "roblox"):
                gentype = '0123456789'
for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        space1 = "-"
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        space2 = "-"
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)

        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+space1+generate4+generate5+space1+generate6+space2+generate7+generate8+generate9+space2+generate10+newline)
            #amazon #Amazon
if(mode == "Amazon"or"amazon"):
     for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)
            #ebay #Ebay
if(mode == "Ebay"or"ebay"):
      for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+newline)
print("Done!!")
print("Enjoy!!")
print("{!} social Media")
print("insta:@cyber.packetz")
print("discord:cyber#1009")
print("server:https://discord.gg/jDN8HjzhTE")
print("{!}code")
print("github:ACE-tr33")
print("link: https://github.com/ACE-t33")
