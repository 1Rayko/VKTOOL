import vk_api
from vk_api import VkUpload
import threading

def q(vk,ask):
    for i in range(ask):
        al=vk.photos.createAlbum(title='vk.com/sudoreboot',description='накрутка фото от vk.com/sudoreboot') 
        print(f"\033[32mАльбом #{i+1} создан\033[39m")
def x(a,b,upload,path):
    j=0
    if a < 0 :
        i=0
        while 1:
            
            if j != len(b):
                try:
                    s = upload.photo(photos=path, album_id=b[j])
                    print(f'\033[32mфото {i+1} загружено в альбом {b[j]}\033[39m')
                    i+=1
                    j+=1
                except:
                        b.remove(j)
                        b+=1
            else:
                j=0
    else:
        for i in range(a):
            if j != len(b):
                try:
                    s = upload.photo(photos=path, album_id=b[j])
                    print(f'\033[32mфото {i+1} загружено в альбом {b[j]}\033[39m')
                    j+=1
                except:
                    b.remove(j)
                    b+=1
            else:
                j=0
def y(a,b,c,upload,path):
    for i in range(c):
        t = threading.Thread(target=x,args=(a,b,upload,path))
        t.start()
def z(vk):
    data=[]
    size=[]
    al= vk.photos.getAlbums()
    for i in range(al['count']):
        if al['items'][i]['size'] != 10000:
            data.append(al['items'][i]['id'])#, al['items'][i]['size'])
            size.append(al['items'][i]['size'])
    return data,size
def main():
    print("Это легкая версия VKTOOL, служащая для накрутки фото\nОт Вас требуется только указать токен, количество фото,путь к фото и количество потоков\nЕсли хотите поставить на бесконечную загрузку, то укажите любое число меньше нуля")
    token=str(input("\033[35mТокен:\033[39m"))
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)
    path=str(input("Путь к фото:"))
    ask=input("\033[33mХотите ли вы создать новые альбомы?(Y/n)\033[39m\n[-->]")
    if ask.lower()=='y':
        ask=int(input("Сколько альбомов создать?\n[-->]"))
        q(vk,ask)
    xdata=input("Параметры в формате x:y\n[-->]").split(':')
    data=z(vk)#для получения неполных альбомов, запихали в массив data
    print(f"альбомов:{len(data[0])}\nколичество фото:{data[1]} ")
    y(int(xdata[0]),data[0],int(xdata[1]),upload,path)#количество(если меньше нуля, то бесконечность),альбомы,потоки, не трогай
main()
