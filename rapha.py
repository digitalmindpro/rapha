#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

import random, os, time, sys
import urllib as urllib
time.sleep(2)
x = os.getlogin()

y = sys.platform
x.upper()
print("\n\t\t======================================================="
      "\n\t\t||\tWELCOME TO DIGITAL-MIND MEDIA DOWNLOADER\t||\n\t\t==========="
      "============================================")
time.sleep(2)
print("\t\t=====+++++++==============================\n\t\t||  SUSU-PICZ 2019.1.0 {FIRST RELEASE}||\n\t\t======="
      "===================================")
time.sleep(2)
print("\t\t=====+++++++==============================\n\t\t||  AUTHOR: RAPHA SAMUEL [DIGITALMIND]||\n\t\t======="
      "===================================")
time.sleep(2)
print("\n\tSelect option\n\t[1]   =>  Image\n\t[2]    =>  Video")
time.sleep(1)

def downloadImage(url):
    name = random.randrange(0, 500)
    default = "Digitalmind_Images_"+str(name)+".png"
    time.sleep(2)
    print("\n\tloading Digital-Waka........>")
    time.sleep(2)
    print("\timage URL is valid")
    print("\t[===                 ]\t[10%] complete")
    urllib.request.urlretrieve(url, default)
    print("\t[====================]\t[100%] complete")
    print("\tImage was successfully downloaded [image name] => ["+default+"]\n"+
          "\tImage was downloaded by: ["+x+"] platform ["+str(y)+"]"+
          "\tThanks for using my services\n\tSigned:\n\tRapha Samuel\n\t@digitalgurus..mind@gmail.com")

def downloadPicture():
    userdefined = input("type the Image URL here:")
    if userdefined != '':
        downloadImage(userdefined)
    else:
        sys.exit()

choice = input("input selection: ")
if int(choice) is 1:
    downloadPicture()
else:
    print("the choice you selected is not supported")
    sys.exit()
