import os

try:
    import click
except:
    print("module click not installed")
    print("-------------------------")
    os.system("pip install click") 
    print("click installed\nrestart vktool-cli")
       

@click.command(help="1337liker's jokes")
def one_jokes():
    os.system('cd ~/VKTOOL && python jokes.py')
@click.command(help="run full version")
def full():
    os.system('cd ~/VKTOOL && python n.py')

    
@click.command(help="run light version")
def light():
    os.system('cd ~/VKTOOL && python light.py')

    
@click.command(help="check and install updates")
def update():
    os.system('cd ~/VKTOOL && git pull')

@click.command(help="install requirements, create an alias in .bashrc / .zshrc")
def install():
    os.system('pip install vk_api vk colorama Pillow python3_anticaptcha')
    print("requirements installed")
    os.system('''echo "alias vktool-cli='python ~/VKTOOL/main.py'" >> ~/.bashrc''')
    os.system('''echo "alias vktool-cli='python ~/VKTOOL/main.py'" >> ~/.zshrc''')
    os.system("cd ~ &&  clear")
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
(https://github.com/kotik06/VKTOOL/)
'''
    pass

cli.add_command(update)
cli.add_command(full)
cli.add_command(light)
cli.add_command(one_jokes)
cli.add_command(install)
if __name__ == "__main__":
    cli()
