# -*- coding: utf-8 -*-
import vk_api,time,random,os
import requests, vk_api, random,time,json,importlib
from threading import Thread
import urllib.request
import threading
from vk_api import VkUpload



try:
    from PIL import Image, ImageDraw, ImageFont
    t=""
except:
    print("PIL не установлен, накрутка фото со счетчиком не доступна")
    t="\033[33m[\033[31mX\033[33m]"
'''
Блин, оптимизация нужна :( [28.09.2021]
ёпересете   пару лишних модулей убрал (Реально хз для чего я их добавил ._.) 




https://github.com/kotik06/VKTOOL

Над утилитой трудились: kotik06 (Я), alonesain, Domen (Хелпанул с накруткой фото) && Huukir (вот ему п***ы дать нужно,расп****й еще тот)

'''

banner = ["""\033[34m____   ________  __. __                .__   
\   \ /   /    |/ _|/  |_  ____   ____ |  |  
 \   Y   /|      < \   __\/  _ \ /  _ \|  |  
  \     / |    |  \ |  | (  <_> |  <_> )  |__
   \___/  |____|__ \|__|  \____/ \____/|____/
                  \/                         
\033[39m by github.com/kotik06""",
    """\033[31m _   _ _   ___              _ 
| | | | | / / |            | |
| | | | |/ /| |_ ___   ___ | |
| | | |    \| __/ _ \ / _ \| |
\ \_/ / |\  \ || (_) | (_) | |
 \___/\_| \_/\__\___/ \___/|_|\033[39m
                              
    by github.com/kotik06"""]
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

 
    #image.show()
os.system('clear')
print(random.choice(banner))
print("""
{1}[{0}1{1}]- накрутка комментариев 
{1}[{0}2{1}]- накрутка постов {2}
{1}[{0}3{1}]- srakoeb2007(beta) {2}
{1}[{0}4{1}]- мульти накрутка коментариев {2}
{1}[{0}5{1}]- парсер пользователей из паблика + добавление их в друзья {2}
{1}[{0}6{1}]{3}- накрутка фото {2}
{1}[{0}7{1}]- скачивание фото {2}
{1}[{0}8{1}]- накрутка сообщений {2}
{1}[{0}9{1}]- отправка заявок в друзья {2}
{1}[{0}10{1}]- 1000-7 статус {2}
""".format(red,yellow,reset,t))
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
    api = vk

    i = 1
    al = '%d коментарий'%(i)
    kaptcha = 'ждем %s секунд от капчи'%(U_time)
    if num == ('1'):
        def krutka():
            vk_session = vk_api.VkApi(token=token)
            vk = vk_session.get_api()
            try :
                for i in range (n):
                    time.sleep(st)
                    try:
                        vk.wall.createComment(owner_id=owner, post_id=post, message=mg)
                        i+=1
                        print('%s%s комментарий отправлен' % (green,i))
                        time.sleep(1)
                        if i == 10:
                            print(kaptcha)
                            i = 1
                            time.sleep(U_time)
                    except vk_api.exceptions.Captcha:
                        print('Капча')
            except vk_api.exceptions.ApiError as error_msg:
                print('invalid token')
        krutka()
    elif num == ('2'):
        def krutka():
            vk_session = vk_api.VkApi(token=token)
            vk = vk_session.get_api()
            try :
                for i in range (n):
                    time.sleep(st)
                    try:
                        vk.wall.createComment(owner_id=owner, post_id=post, message=mg)
                        i+=1
                        print('%s%s комментарий отправлен' % (green,i))
                        time.sleep(1)
                        if i == 10:
                            print(kaptcha)
                            i = 1
                            time.sleep(U_time)
                    except vk_api.exceptions.Captcha:
                        print('Капча')
            except vk_api.exceptions.ApiError as error_msg:
                print('invalid token')
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
    i = 1
    al = '%d пост отправлен' % (i)

    if num == ('1'):
        def spam():
            try:
                for i in range(n):
                    time.sleep(st)
                    try:
                        vk.wall.post(owner_id=-owner,from_group=0,message=mg)
                        i += 1
                        print('%s%s пост отправлен' % (green,i))
                        if i == 10:
                            print(kaptcha)
                            i = 1
                            time.sleep(U_time)
                    except vk_api.exceptions.Captcha :
                        print('Капча')
            except vk_api.exceptions.ApiError as error_msg:
                print('invalid token')

        spam()
    elif num == ('2'):
        def spam():
            try:
                for i in range(n):
                    time.sleep(st)
                    try:
                        vk.wall.post(owner_id=owner,from_group=0,message=mg)
                        i += 1
                        print('%s%s пост отправлен' % (green,i))
                        if i == 10:
                            print(kaptcha)
                            i = 1
                            time.sleep(U_time)
                    except vk_api.exceptions.Captcha :
                        print('Капча')
            except vk_api.exceptions.ApiError as error_msg:
                print('invalid token')
        spam()

elif opt == '3':
    print('!!!srakoeb2007 is beta!!!')
    l = str(input('[1]-add token(profile)\n[2]-add message\n[3]-start\n[-->]'))
    if l == '1':
        tk = str(input('token :'))
        vk_session = vk_api.VkApi(token=tk)#запрос авторизации
        vk = vk_session.get_api()#проверка
        try:

            token = open ('token.txt','a+')
            token.white(str(tk)+'\n')
            token.close()
            print('Записано!')
        
        except vk_api.exceptions.ApiError as error_msg:#если токен инвалид
            print(Fore.RED+'Данные недействительны')

    elif l == '2':
        mg = str(input('message :'))

        me = open ('message.txt','a+')
        me.white(str(mg)+'\n')
        me.close()


    elif l == '3':

        os.system('python3 srakoeb2007.py')

elif opt == '4':
    print("""
{1}[{0}1{1}] - прочитать токены
{1}[{0}2{1}] - добавить
{1}[{0}3{1}] - очистить файл с токенами
{1}[{0}4{1}] - запустить""".format(red,yellow,reset))
    h = str(input('\033[35m[-->]\033[39m'))

    if h == '1':
        file = open("tk.txt", "r",encoding='utf-8')#сука файл
        apikey = file.readlines()
        token = [line.rstrip() for line in apikey]
        b = 0
        print(str(len(token))+' токена(ов)')
        while b<len(token) :
            print(token[b])
               
            b+=1
        file.close()    
    elif h == '2':

        file = open("tk.txt", "a+",encoding='utf-8')
        tk = str(input("token:"))
        file.write(str(tk)+'\n')
        print('done')
        file.close()
    elif h == '3':
        os.system('rm -rv tk.txt')
        os.system('touch tk.txt')

    elif h == '4':
        id = int(input('id (профиля в формате 1, паблика -1):'))
        post = int(input('id поста:'))
        mg = str(input('Сообщение :'))
        U_time =int(input("Задержка отправки (челое число в секундах):"))
        
        file = open("tk.txt", "r",encoding='utf-8')#сука файл
        apikey = file.readlines()
        token = [line.rstrip() for line in apikey]
        b = 0
        print(str(len(token))+' токена(ов)')

        while 1:


            while b<len(token) :
                print(token[b])
                vk_session = vk_api.VkApi(token=token[b])
                vk = vk_session.get_api()
                vk.wall.createComment(owner_id=id, post_id=post, message=mg)
                print('send')
                time.sleep(U_time)
                b+=1
                continue
            b=0

elif opt == '5':
    
    os.system('python parser.py')

elif opt == '6':
    #print("спасибо за помощь Domen'у")
    j=str(input('[1]-накрутка своих фото\n[2]-накрутка манулов :D\n[3]-накрутка своих фото с счетчиком\n[4]-накрутка с потоками\n[-->]'))
    if j =='1':
        s=str(input('[1]-token\n[2]-login&password\n[-->] '))
        b=0
        if s =='2':
            lo=str(input("Логин: "))
            pa=str(input("Пароль: "))
            vk_session = vk_api.VkApi(login=lo, password=pa, app_id='2685278')
            vk_session.auth(token_only=True)
            longpoll = VkLongPoll(vk_session)
            upload = VkUpload(vk_session)
            pot=str(input('Имя файла(или путь к нему): '))
            al=int(input('id альбома:'))
            count = str(input("Количество фотографий(бесконечность = qq): "))
            b = 0
            if count == 'qq':
                b=0
                while 1:
                    s = upload.photo(photos=pot, album_id=al)
                    b += 1
                    print(str(b)+"\033[32m фото загружено\033[39m")
            else:        
                while b != int(count):
                    s = upload.photo(photos=pot, album_id=al)
                    b += 1
                    print(str(b)+"\033[32m фото загружено\033[39m")
        else:
            tk=str(input("token: "))
            vk_session = vk_api.VkApi(token=tk,app_id='2685278')
           # vk_session.auth(token_only=True)
            longpoll = VkLongPoll(vk_session)
            upload = VkUpload(vk_session)
            pot=str(input('Имя файла(или путь к нему): '))
            al=int(input('id альбома:'))
            count = str(input("Количество фотографий(бесконечность = qq): "))
            b = 0
            if count == 'qq':
                b=0
                while 1:
                    s = upload.photo(photos=pot, album_id=al)
                    b += 1
                    print(str(b)+"\033[32m фото загружено\033[39m")
            else:        
                while b != int(count):
                    s = upload.photo(photos=pot, album_id=al)
                    b += 1
                    print(str(b)+"\033[32m фото загружено\033[39m")
    elif j == "2":
        s=str(input('[1]-token\n[2]-login&password\n[-->] '))
        if s =='2':
            lo=str(input("Логин: "))
            pa=str(input("Пароль: "))
            vk_session = vk_api.VkApi(login=lo, password=pa, app_id='2685278')
            vk_session.auth(token_only=True)
            longpoll = VkLongPoll(vk_session)
            upload = VkUpload(vk_session)
            al=int(input('id альбома:'))
            count = str(input("Количество фотографий(бесконечность = qq): "))
            start=int(input('Со скольки начать счет манулов :'))
            j=0
            b=start
            if count == 'qq':
            
                while 1:

                    image = Image.open("manul.jpg")

                    font = ImageFont.truetype("arial.ttf", 25)
                    drawer = ImageDraw.Draw(image)
                    drawer.text((150, 100), f"{b} манулов", font=font, fill='black')
                    image.save(f'manul{b}.jpg')
                    time.sleep(1)
                    try:
                        s = upload.photo(photos=f'manul{b}.jpg', album_id=al)
                    
                        os.remove(f'manul{b}.jpg')
                        b += 1
                        j+=1
                        print(str(j)+"\033[32m фото загружено\033[39m")
                    except:
                        time.sleep(10)
            else:        
                while j != int(count):
                    image = Image.open("manul.jpg")

                    font = ImageFont.truetype("arial.ttf", 25)
                    drawer = ImageDraw.Draw(image)
                    drawer.text((150, 100), f"{b} манулов", font=font, fill='black')

                    image.save(f'manul{b}.jpg')
                    time.sleep(1)
                    try:
                        s = upload.photo(photos=f'manul{b}.jpg', album_id=al)
                    
                        os.remove(f'manul{b}.jpg')
                        j += 1
                        b+=1
                        print(str(j)+"\033[32m фото загружено\033[39m")
                    except:
                        time.sleep(10)

        else:
            tk=str(input("token: "))
            vk_session = vk_api.VkApi(token=tk,app_id='2685278')
           # vk_session.auth(token_only=True)
            longpoll = VkLongPoll(vk_session)
            upload = VkUpload(vk_session)
            al=int(input('id альбома:'))
            count = str(input("Количество фотографий(бесконечность = qq): "))
            start=int(input('Со скольки начать счет манулов :'))
            j=0
            b=start
            if count == 'qq':
            
                while 1:

                    image = Image.open("manul.jpg")

                    font = ImageFont.truetype("arial.ttf", 25)
                    drawer = ImageDraw.Draw(image)
                    drawer.text((150, 100), f"{b} манулов", font=font, fill='black')
                    image.save(f'manul{b}.jpg')
                    time.sleep(1)
                    try:
                        s = upload.photo(photos=f'manul{b}.jpg', album_id=al)
                    
                        os.remove(f'manul{b}.jpg')
                        b += 1
                        j+=1
                        print(str(j)+"\033[32m фото загружено\033[39m")
                    except:
                        time.sleep(10)
            else:        
                while j != int(count):
                    image = Image.open("manul.jpg")

                    font = ImageFont.truetype("arial.ttf", 25)
                    drawer = ImageDraw.Draw(image)
                    drawer.text((150, 100), f"{b} манулов", font=font, fill='black')

                    image.save(f'manul{b}.jpg')
                    time.sleep(1)
                    try:
                        s = upload.photo(photos=f'manul{b}.jpg', album_id=al)
                    
                        os.remove(f'manul{b}.jpg')
                        j += 1
                        b+=1
                        print(str(j)+"\033[32m фото загружено\033[39m")
                    except:
                        time.sleep(10)
                    #print(str(j)+"\033[32m фото загружено\033[39m")
    elif j == "3":
        s=str(input('[1]-token\n[2]-login&password\n[-->] '))
        if s =='2':
            lo=str(input("Логин: "))
            pa=str(input("Пароль: "))
            vk_session = vk_api.VkApi(login=lo, password=pa, app_id='2685278')
            vk_session.auth(token_only=True)
            longpoll = VkLongPoll(vk_session)
            upload = VkUpload(vk_session)
            al=int(input('id альбома:'))
            p=str(input("Путь к исходному фото:"))
            kogo=str(input("Кого считать?(манулов, собачек,кошек):"))
            count = str(input("Количество фотографий(бесконечность = qq): "))
            start=int(input('Со скольки начать счет:'))
            j=0
            b=start
            if count == 'qq':
            
                while 1:

                    image = Image.open(p)

                    font = ImageFont.truetype("arial.ttf", 25)
                    drawer = ImageDraw.Draw(image)
                    drawer.text((150, 100), f"{b} {kogo}", font=font, fill='black')
                    image.save(f'{p}{b}.jpg')
                    time.sleep(1)
                    try:
                        s = upload.photo(photos=f'{p}{b}.jpg', album_id=al)
                    
                        os.remove(f'{p}{b}.jpg')
                        b += 1
                        j+=1
                        print(str(j)+"\033[32m фото загружено\033[39m")
                    except:
                        time.sleep(10)
            else:        
                while j != int(count):
                    image = Image.open(p)

                    font = ImageFont.truetype("arial.ttf", 25)
                    drawer = ImageDraw.Draw(image)
                    drawer.text((150, 100), f"{b} {kogo}", font=font, fill='black')

                    image.save(f'{p}l{b}.jpg')
                    time.sleep(1)
                    try:
                        s = upload.photo(photos=f'{p}{b}.jpg', album_id=al)
                    
                        os.remove(f'{p}{b}.jpg')
                        j += 1
                        b+=1
                        print(str(j)+"\033[32m фото загружено\033[39m")
                    except:
                        time.sleep(10)

        else:
            tk=str(input("token: "))
            vk_session = vk_api.VkApi(token=tk,app_id='2685278')
           # vk_session.auth(token_only=True)
            longpoll = VkLongPoll(vk_session)
            upload = VkUpload(vk_session)
            al=int(input('id альбома:'))
            p=str(input("Путь к исходному фото:"))
            kogo=str(input("Кого считать?(манулов, собачек,кошек):"))
            count = str(input("Количество фотографий(бесконечность = qq): "))
            start=int(input('Со скольки начать счет:'))
            j=0
            b=start
            if count == 'qq':
            
                while 1:

                    image = Image.open(p)

                    font = ImageFont.truetype("arial.ttf", 25)
                    drawer = ImageDraw.Draw(image)
                    drawer.text((150, 100), f"{b} {kogo}", font=font, fill='black')
                    image.save(f'{p}{b}.jpg')
                    time.sleep(1)
                    try:
                        s = upload.photo(photos=f'{p}{b}.jpg', album_id=al)
                    
                        os.remove(f'{p}{b}.jpg')
                        b += 1
                        j+=1
                        print(str(j)+"\033[32m фото загружено\033[39m")
                    except:
                        time.sleep(10)
            else:        
                while j != int(count):
                    image = Image.open(p)

                    font = ImageFont.truetype("arial.ttf", 25)
                    drawer = ImageDraw.Draw(image)
                    drawer.text((150, 100), f"{b} {kogo}", font=font, fill='black')

                    image.save(f'{p}l{b}.jpg')
                    time.sleep(1)
                    try:
                        s = upload.photo(photos=f'{p}{b}.jpg', album_id=al)
                    
                        os.remove(f'{p}{b}.jpg')
                        j += 1
                        b+=1
                        print(str(j)+"\033[32m фото загружено\033[39m")
                    except:
                        time.sleep(10)
                    #print(str(j)+"\033[32m фото загружено\033[39m")        
    elif j =="4":
        b = int(input("Количество потоков:"))
        def a(tk,ph,al):
            
            vk_session = vk_api.VkApi(token=tk,app_id='2685278')
             # vk_session.auth(token_only=True)
            longpoll = VkLongPoll(vk_session)
            upload = VkUpload(vk_session)

            b = 0

            while 1:
                try:
                    s = upload.photo(photos=ph, album_id=al)
                    print(str(b)+" фото загружено")
                    b+=1
                except Exception as e:
                    print(e)
        tk=str(input('Токен: '))
        ph=str(input('Путь к фото: '))
        al=int(input('id альбома:'))
        for i in range(b):
            t = threading.Thread(target=a, args=(tk,ph,al))
            t.start()

elif opt == '7':
    def s():
        url = str(input("Ссылка на фото: "))

        img = urllib.request.urlopen(url).read()
        out = open("img.jpg", "wb")
        out.write(img)
        out.close
        print("Фото сохранено как img.jpg")
    s()

elif opt =='8':
    #targets=map(str, input("Введите id людей, которым начать накрутку через пробел(Важно, чтобы все эти пользователи были в друзьях у ботов):").split())
    print('[1]-добавть ботов в файл bots.txt\n[2]-прочитать токены\n[3]-очистить файл с токенами\n[4]-запустить накрутку\n')
    pososo= str(input("[->>]"))
    
   
    if pososo == "1":
        file = open("bots.txt", "a+",encoding='utf-8')
        t=input("Введите токен:")
        file.write(f"{t}\n")
        file.close()
    elif pososo == "2":
        file = open("bots.txt", "r",encoding='utf-8')
        print(file.read())
        file.close()
    elif pososo == "3":
        os.remove('bots.txt')
        os.system('touch bots.txt')
    elif pososo == "4":
        targets = list(input("Введите id людей, которым начать накрутку, через пробел(Важно, чтобы все эти пользователи были в друзьях у ботов):").split())
        file = open("bots.txt", "r",encoding='utf-8')#сука файл
        apikey = file.readlines()
        token = [line.rstrip() for line in apikey]
        b = 0
        print(str(len(token))+' токена(ов)')
        while 1:
            while b<len(token) :

                #print(token[b])
                vk_session = vk_api.VkApi(token=token[b])
                try:
                    vk = vk_session.get_api()
                    try:
                        vk.messages.createChat(user_ids=targets,title="накрутка by sudoreboot")
                        print("{0}Беседа создана с аккаунта{1}".format(green,reset),vk.account.getProfileInfo()["first_name"],vk.account.getProfileInfo()["last_name"])
                    except Exception as e:
                        print("{0}error{1}".format(red,reset),e,vk.account.getProfileInfo()["first_name"],vk.account.getProfileInfo()["last_name"])
                except Exception as e:
                    print("{0}error{1}".format(red,reset),e)
                b+=1
                continue
            time.sleep(20)
            b=0

elif opt == '9':
    u=int(input('id пользователя: '))
    file = open("bots.txt", "r",encoding='utf-8')#сука файл
    apikey = file.readlines()
    token = [line.rstrip() for line in apikey]
    b = 0
    print(str(len(token))+' токена(ов)')
    
    while b<len(token) :

                #print(token[b])
        vk_session = vk_api.VkApi(token=token[b])
        try:
            vk = vk_session.get_api()
            vk.friends.add(user_id=u,text="прими бота")
            print("{0}Заявка отправлена с аккаунта{1}".format(green,reset),vk.account.getProfileInfo()["first_name"],vk.account.getProfileInfo()["last_name"])
            b+=1
        except Exception as e:
            print("{0}error{1}".format(red,reset),e)
            b+=1

elif opt == '10':

    plaseholder = str(input("[1]-token\n[2]-login+password\n[-->]"))
    if plaseholder == '1':
        token=str(input("Введите токен:"))
        vk_session = vk_api.VkApi(token=token)
        try:
            vk = vk_session.get_api()
            vk.account.saveProfileInfo(status='1000-7=?')
            i=1000
            while 1:
                vk.account.saveProfileInfo(status=f'{i}-7={i-7}')
                if i < 0:
                    i=1000
                else:
                    i-=7
                print("zxc")
                time.sleep(1)
        except Exception as e:
            print("{0}error{1}".format(red,reset),e)

    else:
        lo=str(input("Введите логин:"))
        pa= str(input("Введите пароль:"))
        vk_session = vk_api.VkApi(login=lo, password=pa, app_id='2685278')
        #vk_session.auth(token_only=True)
        try:
            vk = vk_session.get_api()
            vk.account.saveProfileInfo(status='1000-7=?')

            i=1000
            while 1:
                vk.account.saveProfileInfo(status=f'{i}-7={i-7}')
                if i < 0:
                    i=1000
                else:
                    i-=7
                print("zxc")
                time.sleep(1)
                
        except Exception as e:
            print("{0}error{1}".format(red,reset),e)
