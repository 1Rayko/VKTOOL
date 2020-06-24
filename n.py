# -*- coding: utf-8 -*-
import vk_api,time,random,vk,os
from colorama import init
import requests, vk_api, random,time,traceback,json,importlib
try:
    import info
    import pod
except:
    pass
from threading import Thread
import traceback
from vk_api.longpoll import VkLongPoll, VkEventType, VkChatEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from python3_anticaptcha import ImageToTextTask
from python3_anticaptcha import errors
banner = ["""\033[34m____   ________  __. __                .__   
\   \ /   /    |/ _|/  |_  ____   ____ |  |  
 \   Y   /|      < \   __\/  _ \ /  _ \|  |  
  \     / |    |  \ |  | (  <_> |  <_> )  |__
   \___/  |____|__ \|__|  \____/ \____/|____/
                  \/                         
                  \033[39m by @kotik06 (sudoreboot2020)""",
    """\033[31m _   _ _   ___              _ 
| | | | | / / |            | |
| | | | |/ /| |_ ___   ___ | |
| | | |    \| __/ _ \ / _ \| |
\ \_/ / |\  \ || (_) | (_) | |
 \___/\_| \_/\__\___/ \___/|_|\033[39m
                              
                              by @kotik06 (sudoreboot2020)""",
    """\033[35m\  /|/_|_ _  _ |
 \/ |\ | (_)(_)|
                \033[39m by @kotik06 (sudoreboot2020)"""]
red = '\033[31m'
yellow = '\033[33m'
reset = '\033[39m'
mag = '\033[35m'
green = '\033[32m'
#ESC [ 30 m      # black
#ESC [ 31 m      # red
#ESC [ 32 m      # green
#ESC [ 33 m      # yellow
#ESC [ 34 m      # blue
#ESC [ 35 m      # magenta
#ESC [ 36 m      # cyan
#ESC [ 37 m      # white
#ESC [ 39 m      # reset
os.system('clear')
print(random.choice(banner))
print("""
{1}[{0}1{1}]- накрутка комментариев 
{1}[{0}2{1}]- накрутка постов {2}
{1}[{0}3{1}]- srakoeb2007(beta) {2}
""".format(red,yellow,reset))
opt = str(input('\033[35m[-->]\033[39m'))

if opt=='1':
    token = str(input('\033[35mВведите токен:'))
    a = """{1}[{0}1{1}] - комментарии к посту в группе\n{1}[{0}2{1}] - коментарии к посту на стене пользователя\n""".format(red,yellow)
    print(a)
    num = str(input('\033[35m[-->]\033[39m'))
    owner = int(input("\033[35mВведите числовой id профиля/группы(Указывайте только числами):\033[39m"))
    post = int(input("\033[35mВведите числовой id поста(Указывайте только числами):\033[39m"))
    mg =  str(input("\033[35mВведите коментарий:\033[39m"))
    ahtung = '''{0}У большинства пользователей капча!!!{1}'''.format(red,reset)
    print(ahtung)
    n = int(input('Сколько коментариев (от 1 до 500):\033[39m'))
    U_time = int(input('Введите задержку от капчи  (ЦЕЛЫМ Числом в секундах желательно >10 сек):'))
    st = int(input('Введите задержку отправки коментария (ЦЕЛЫМ Числом в секундах):'))
    def login ():
        if token == '':
            return True
        else:
            session = vk.Session(access_token=token)
            return vk.API(session ,v='5.92', lang='ru')
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    api = vk
    i = 1
    al = '%d коментарий'%(i)
    kaptcha = 'ждем %s секунд от капчи'%(U_time)
    if num == ('1'):
        def krutka():
            for i in range (n):
                time.sleep(st)
                vk.wall.createComment(owner_id=-owner, post_id=post, message=mg)
                i+=1
                print('%s%s комментарий отправлен' % (green,i))
                if i == 10:
                    print(kaptcha)
                    i = 1
                    time.sleep(U_time)


        krutka()
    elif num == ('2'):
        def krutka():
            for i in range (n):
                time.sleep(st)
                vk.wall.createComment(owner_id=owner, post_id=post, message=mg)
                i+=1
                print('%s%s комментарий отправлен' % (green,i))
                time.sleep(1)
                if i == 10:
                    print(kaptcha)
                    i = 1
                    time.sleep(U_time)


        krutka()

elif opt == '2':
    token = str(input('\033[35mВведите токен:'))
    a = """{1}[{0}1{1}] -  спам  в группу\n{1}[{0}2{1}] - спам на стену пользователя\n""".format(red, yellow)
    print(a)
    num = str(input('\033[35m[-->]\033[39m'))
    owner = int(input("\033[35mВведите числовой id профиля/группы(Указывайте только числами):\033[39m"))
    mg = str(input("\033[35mВведите содержание поста:\033[39m"))
    ahtung = '''{0}У большинства пользователей капча!!!{1}'''.format(red, reset)
    print(ahtung)
    n = int(input('Сколько постов (от 1 до 500):\033[39m'))
    st = int(input('Введите задержку отправки коментария (ЦЕЛЫМ Числом в секундах):'))
    U_time = int(input('Введите задержку от капчи  (ЦЕЛЫМ Числом в секундах желательно 10 сек):'))

    def login():
        if token == '':
            return True
        else:
            session = vk.Session(access_token=token)
            return vk.API(session, v='5.92', lang='ru')


    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    api = vk
    i = 1
    al = '%d пост отправлен' % (i)

    if num == ('1'):
        def spam():
            for i in range(n):
                time.sleep(st)
                vk.wall.post(owner_id=-owner,from_group=0,message=mg)
                i += 1
                print('%s%s пост отправлен' % (green,i))
                if i == 10:
                    print(kaptcha)
                    i = 1
                    time.sleep(U_time)


        spam()
    elif num == ('2'):
        def spam():
            for i in range(n):
                time.sleep(st)
                vk.wall.post(owner_id=owner, message=mg)
                i += 1
                print('%s%s пост отправлен' % (green,i))
                time.sleep(1)
                if i >= 10:
                    print(kaptcha)
                    i = 1
                    time.sleep(U_time)


        spam()

elif opt == '3':
    print('!!!srakoeb2007 is beta!!!')
    l = str(input('[1]-add token(profile)\n[2]-add message\n[3]-start'))
    if l == '1':
        tk = str(input('token :'))

        token = open ('token.txt','a+')
        token.white(str(tk)+'\n')
        token.close()

    elif l == '2':
        mg = str(input('message :'))

        me = open ('message.txt','a+')
        me.white(str(mg)+'\n')
        me.close()


    elif l == '3':

        os.system('python3 srakoeb2007.py')