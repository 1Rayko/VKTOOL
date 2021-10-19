# -*- coding: utf-8 -*-
import time,os,requests, vk_api, random,time,json,importlib,urllib.request
import threading
from vk_api import VkUpload

os.system('clear')

try:
    from PIL import Image, ImageDraw, ImageFont
    t=""
except:
    print("Pillow не установлен, накрутка фото со счетчиком не доступна")
    t="\033[33m[\033[31mX\033[33m]"
    time.sleep(0.1)
    
    
'''
Блин, оптимизация нужна :( [28.09.2021]
ёпересете   пару лишних модулей убрал (Реально хз для чего я их добавил ._.) 




https://github.com/kotik06/VKTOOL

Над утилитой трудились: kotik06 (Я), alonesain, Domen (Хелпанул с накруткой фото) && Huukir (вот ему п***ы дать нужно,расп****й еще тот)

Нужно переписать на этот ваш 3.10 че (18.10.2021)
(19.10.2021) все еще переписываю

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
opt = int(input('\033[35m[-->]\033[39m'))

match opt:
    case 1:
        token = str(input('\033[35mВведите токен:'))
        #print("{1}[{0}1{1}] - комментарии к посту в группе\n{1}[{0}2{1}] - коментарии к посту на стене пользователя\n".format(red,yellow))
        #num = str(input('\033[35m[-->]\033[39m'))
        data = str(input("\033[35mВведите id поста( В формате 1_10  ):\033[39m")).split('_')
        #post = int(input("\033[35mВведите числовой id поста(Указывайте только числами):\033[39m"))
        mg =  str(input("\033[35mВведите коментарий:\033[39m"))
        n = int(input('Количество коментариев:\033[39m'))
        st = int(input('Введите задержку между отправкой коментариев:'))      
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        
        try :
            i=1
            while i<=n:
                try:
                    vk.wall.createComment(owner_id=int(data[0]), post_id=int(data[1]), message=mg)
                    print('%s%s комментарий отправлен' % (green,i))
                    i+=1
                    time.sleep(st)
                except vk_api.exceptions.Captcha:
                    print('Капча. Спим 10 сек')
                    time.sleep(10)
                    
        except vk_api.exceptions.ApiError as error_msg:
            print('Недействительный токен')
        #krutka()
    case 2:
        token = str(input('\033[35mВведите токен:'))        
        data = int(input("\033[35mВведите id страницы/группы( В формате 1/-1):\033[39m"))
        mg = str(input("\033[35mВведите текст поста:\033[39m"))
        n = int(input('Количество постов :\033[39m'))
        st = int(input('Введите задержку между созданием постов :'))
        #U_time = int(input('Введите задержку от капчи  (ЦЕЛЫМ Числом в секундах желательно 10 сек):'))

        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        try:
            i=1
            while i<=n: 
                try:
                    vk.wall.post(owner_id=data,from_group=0,message=mg)
                    print('%s%s пост отправлен' % (green,i))
                    i+=1
                except vk_api.exceptions.Captcha :
                    print('Капча. Cпим 10 сек')
                    time.sleep(10)
        except vk_api.exceptions.ApiError as error_msg:
            print('Недействительный токен')

    case 3:
    #print('!!!srakoeb2007 is beta!!!')
        l = int(input('[1]-Добавить токен профиля\n[2]-Добавить сообщение\n[3]-запустить\n[-->]'))
        match l:

            case 1:
                tk = str(input('Токен :'))
                vk_session = vk_api.VkApi(token=tk)#запрос авторизации
                vk = vk_session.get_api()#проверка
                try:

                    token = open ('token.txt','a+')
                    token.white(str(tk)+'\n')
                    token.close()
                    print('Записано')
                
                except vk_api.exceptions.ApiError as error_msg:#если токен инвалид
                    print(Fore.RED+'Данные недействительны')

            case 2:
                mg = input('Текст сообщения :')
                f = open ('message.txt','a+')
                f.write(str(mg)+'\n')
                f.close()
                print("Записано")

            case 3:

                os.system('python3 srakoeb2007.py')
            case _:
                print("Инвалидный параметр")
    case 4:
        print("{1}[{0}1{1}] - прочитать токены\n{1}[{0}2{1}] - добавить\n{1}[{0}3{1}] - очистить файл с токенами\n{1}[{0}4{1}] - запустить".format(red,yellow,reset))
        h = int(input('\033[35m[-->]\033[39m'))
        match h:
            case 1:
                file = open("tk.txt", "r",encoding='utf-8')#сука файл
                apikey = file.readlines()
                token = [line.rstrip() for line in apikey]
                b = 0
                print("В файле 'tk.txt' "+str(len(token))+' токена(ов)')
                while b<len(token) :
                    print(token[b])     
                    b+=1
                file.close()    
            case 2:

                file = open("tk.txt", "a+",encoding='utf-8')
                tk = str(input("Токен:"))
                file.write(str(tk)+'\n')
                file.close()
                print('Записано')
            case 3:
                os.system('rm -rv tk.txt')
                os.system('touch tk.txt')

            case 4:
                data = str(input("\033[35mВведите id поста( В формате 1_10  ):\033[39m")).split('_')
                mg = str(input('Сообщение :'))
                file = open("tk.txt", "r",encoding='utf-8')#сука файл
                apikey = file.readlines()
                token = [line.rstrip() for line in apikey]
                i = 0
                print(str(len(token))+' токена(ов)')
                while 1:
                    while i<len(token) :
                        print(token[i])
                        vk_session = vk_api.VkApi(token=token[b])
                        vk = vk_session.get_api()
                        vk.wall.createComment(owner_id=int(data[0]), post_id=int(data[1]), message=mg)
                        print('Комментарий отправлен. Спим 5 сек')
                        time.sleep(5)
                        b+=1
                    b=0

    case 5:
    
        os.system('python parser.py')

    case 6:
        #print("спасибо за помощь Domen'у")
        j=int(input('[1]-накрутка своих фото\n[2]-накрутка манулов :D\n[3]-накрутка своих фото с счетчиком\n[4]-накрутка с потоками\n[-->]'))
        match j:
            case 1:
                s=int(input('[1]-Авторизация по токену\n[2]-Авторизация по логину и паролю\n[-->] '))
                
                b=0
                match s:
    
                    case 2:
                        lo=str(input("Логин: "))
                        pa=str(input("Пароль: "))
                        vk_session = vk_api.VkApi(login=lo, password=pa, app_id='2685278')
                    case _:
                        tk=str(input("Токен: "))
                        vk_session = vk_api.VkApi(token=tk,app_id='2685278')
                
                
                upload = VkUpload(vk_session)
                pot=str(input('Имя файла(или путь к нему): '))
                al=int(input('id альбома:'))
                count = str(input("Количество фотографий(бесконечность = qq): "))
                b = 0
                match count:
                    case 'qq':
                        b=0
                        while 1:
                            s = upload.photo(photos=pot, album_id=al)
                            b += 1
                            print(str(b)+"\033[32m фото загружено\033[39m")
                    case _ :        
                        while b != int(count):
                            s = upload.photo(photos=pot, album_id=al)
                            b += 1
                            print(str(b)+"\033[32m фото загружено\033[39m")
            case 2:
                s=str(input('[1]-Авторизация по токену\n[2]-Авторизация по логину и паролю\n[-->] '))
                match s:
                    case '2':
                        lo=str(input("Логин: "))
                        pa=str(input("Пароль: "))
                        vk_session = vk_api.VkApi(login=lo, password=pa, app_id='2685278')

                    case _ :
                        tk=str(input("token: "))
                        vk_session = vk_api.VkApi(token=tk,app_id='2685278')
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
            case 3:
                s=str(input('[1]-Авторизация по токену\n[2]-Авторизация по логину и паролю\n[-->] '))
                match s:
                    case 2:
                
                        lo=str(input("Логин: "))
                        pa=str(input("Пароль: "))
                        vk_session = vk_api.VkApi(login=lo, password=pa, app_id='2685278')
                    case _:
                        tk=str(input("token: "))
                        vk_session = vk_api.VkApi(token=tk,app_id='2685278')
                       # vk_session.auth(token_only=True)
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
            case 4:
                b = int(input("Количество потоков:"))
                def a(tk,ph,al):
                    
                    vk_session = vk_api.VkApi(token=tk,app_id='2685278')
                     # vk_session.auth(token_only=True)

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

    case 7:
    
        url = str(input("Ссылка на фото: "))

        img = urllib.request.urlopen(url).read()
        out = open("img.jpg", "wb")
        out.write(img)
        out.close()
        print("Фото сохранено как img.jpg")
    
    case 8:
        #targets=map(str, input("Введите id людей, которым начать накрутку через пробел(Важно, чтобы все эти пользователи были в друзьях у ботов):").split())
        print('[1]-добавть ботов в файл bots.txt\n[2]-прочитать токены\n[3]-очистить файл с токенами\n[4]-запустить накрутку\n')
        pososo= str(input("[->>]"))
        
        match pososo: 
            case "1":
                file = open("bots.txt", "a+",encoding='utf-8')
                t=input("Введите токен:")
                file.write(f"{t}\n")
                file.close()
            case "2":
                file = open("bots.txt", "r",encoding='utf-8')
                print(file.read())
                file.close()
            case "3":
                os.remove('bots.txt')
                os.system('touch bots.txt')
            case "4":
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

    case 9:
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
                vk.friends.add(user_id=u,text="github.com/kotik06/VKTOOL")
                print("{0}Заявка отправлена с аккаунта{1}".format(green,reset),vk.account.getProfileInfo()["first_name"],vk.account.getProfileInfo()["last_name"])
                b+=1
            except Exception as e:
                print("{0}error{1}".format(red,reset),e)
                b+=1

    case 10:

        plaseholder = int(input("[1]-Авторизация по токену\n[2]-Авторизация по логину и паролю\n[-->]"))
        match plaseholder:

            case 1:
                token=str(input("Введите токен:"))
                vk_session = vk_api.VkApi(token=token)
            case _:
                lo=str(input("Введите логин:"))
                pa= str(input("Введите пароль:"))
                vk_session = vk_api.VkApi(login=lo, password=pa, app_id='2685278')
                #vk_session.auth(token_only=True)
        try:
            vk = vk_session.get_api()
            

            i=1000
            while 1:
                vk.account.saveProfileInfo(status=f'{i}-7={i-7}')
                if i < 0:
                    i=1000
                else:
                    i-=7
                print(f"{i=}")
                time.sleep(1)
                
        except Exception as e:
            print("{0}error{1}".format(red,reset),e)
