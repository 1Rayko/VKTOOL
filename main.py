#!/usr/bin/env python3
import os

try:
    import click
except:
    print("module click not installed")
    print("-------------------------")
    os.system("python3.10 -m pip install click") 
    print("click installed\nrestart vktool-cli")
@click.command(help="Upload history")
def story():
    os.system("cd ~/VKTOOL && python3.10 story.py")

@click.command(help="1337liker's jokes")
def one_jokes():
    os.system('cd ~/VKTOOL && python3.10 jokes.py')
@click.command(help="run full version")
def full():
    os.system('cd ~/VKTOOL && python3.10 n.py')

@click.command(help="run light version")
def light():
    os.system('cd ~/VKTOOL && python3.10 light.py')

@click.command(help="check and install updates")
def update():
    os.system('cd ~/VKTOOL && git pull && sudo python3.10 main.py install')

@click.command(help="install requirements, install vktool-cli to /usr/local/bin")
def install():
    os.system('python3.10 -m pip install vk_api vk colorama Pillow python3_anticaptcha')
    print("requirements installed")
    #os.system("bash ~/VKTOOL/install.sh")
    #vktool="#!/bin/bash\npython ~/VKTOOL/main.py"
    #os.system(f'echo "{vktool}" >> /usr/local/bin/vktool-cli')
    user = os.getlogin()
    # os.system(f"cp /home/{user}/VKTOOL/main.py /usr/local/bin/vktool-cli")
    os.system("cp /home/{}/VKTOOL/main.py /usr/local/bin/vktool-cli".format(user))
    os.system("chmod +x /usr/local/bin/vktool-cli")
    print("Done")
@click.group()
def cli():
    '''
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
'''
    pass

cli.add_command(update)
cli.add_command(full)
cli.add_command(light)
cli.add_command(one_jokes)
cli.add_command(install)
cli.add_command(story)
if __name__ == "__main__":
    cli()
