#!/usr/bin/python3.10 
import os,sys


def vkhelp():
    print( '''
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWNXK00KK0K000KKKKKKK00KXNWWWWWWWW
    WWWWWWKxlcccccccccccccccccccccclxKWWWWWW
    WWWWWKo;lk00000K000KKKKK000K00kc;oKWWWWW
    WWWWWO::kWWWWWWWWWWWWWWWWWWWWWNk::OWWWWW
    WWWWWO::OWWWWWWWWWWWWWWWWWWWWWWO::OWWWWW
    WWWWWO::OWN0kkKNXOdddONWXOkk0NWO::OWWWWW
    WWWWWO::OWNx:,cOXx;,,lKXd;,:kNWO::OWWWWW
    WWWWWO::OWWXx:,:do;,,cdl;;l0NWWO::OWWWWW
    WWWWWO::OWWWNOc;,,,,,,;;,;oKNWWO::OWWWWW
    WWWWWO::OWWWWWKxl:;;;cxxc;;ckNWO::OWWWWW
    WWWWWO::OWWWWWWWNK0O0KNWX0OOKNWO::OWWWWW
    WWWWWO::OWWWWWWWWWWWWWWWWWWWWWWO::OWWWWW
    WWWWW0c;dXNWWWWWWWWWWWWWWWWWWWXx;c0WWWWW
    WWWWWNkc:loddddddddddddddddddol:ckNWWWWW
    WWWWWWNKOxddddddddddddddddddddxOXWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    (https://github.com/1Rayko/VKTOOL/)
    
    Usage: vktool-cli (func) (args)
    func:

        help:
            -h || --help

        version:
            -v || --version

        full: 
            -f || full

        light:
            -l || light
        story:
            -s || story
        jokes:
            -j || jokes
        update:
            -u || update

    args: 
        not invent :D


    ''')



 
if len(sys.argv)>1:
    match sys.argv[1].strip():
        case "-h"   | "--help":
            vkhelp()
        case "-v"   | "--version":
            print(3.0 )
        case "-f"   | "full" : 
           os.system("cd ~/VKTOOL && python n.py") 
        case "-l"   | "light": 
           os.system("cd ~/VKTOOL && python light.py") 
        case "-s"   | "story": 
           os.system("cd ~/VKTOOL && python story.py") 
        case "-j"   | "jokes":
           os.system("cd ~/VKTOOL && python jokes.py") 
        case "-u"   | "update":
            os.system("cd ~/VKTOOL && git pull && bash install")
        case _:
            vkhelp()
else:
    vkhelp()
