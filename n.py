import vk_api,time,random,vk,os
from colorama import init
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
os.system('clear')
print(random.choice(banner))
token = str(input('\033[35mВведите токен:'))
num = str(input('\033[35m[1] - комментарии к посту в группе\n[2] - коментарии к посту на стене пользователя\n[-->]\033[39m'))
owner = int(input("\033[35mВведите числовой id профиля/группы(Указывайте только числами):\033[39m"))
post = int(input("\033[35mВведите числовой id поста(Указывайте только числами):\033[39m"))
mg =  str(input("\033[35mВведите коментарий:\033[39m"))
n = int(input('Сколько коментариев (от 1 до 500):\033[39m'))


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

if num == ('1'):
    def krutka():
        for i in range (n):
            vk.wall.createComment(owner_id=-owner, post_id=post, message=mg)
            i+=1
            print('%s коментарий отправлен'%(i))
            if i >= 499:
                print('Капча :( выключай и жди 5 мин')
                i = 0

    krutka()
elif num == ('2'):
    def krutka():
        for i in range (n):
            vk.wall.createComment(owner_id=owner, post_id=post, message=mg)
            i+=1
            print('%s коментарий отправлен'%(i))
            if i >= 499:
                print('Капча :( выключай и жди 5 мин')
                i = 0

    krutka()