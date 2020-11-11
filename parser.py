# -*- coding: utf-8 -*-
'''импорты'''
#НАПИСАЛ @kotik06 (sudoreboot2020) 
#если уберешь , то ты - гей :D
import vk_api#импорт вк апи
from os import system as suka# из модуля ос импортируем функцию систем (для работы с системой) обращаемся к ней через suka
from time import sleep as maksim_eblan# тут аналогично строке выше
from colorama import init, Fore, Back, Style# из колорамы импорт функций  init, Fore, Back, Style

init(convert=True)#обращение к колорамовской херне 
def parser(tk,id_pab,n):
	"""функция парсер с входяцими агрументами"""
	if n >= 1000:
		n = 1000
	token = tk#токен = переменной тк
	vk_session = vk_api.VkApi(token=token)#запрос авторизации
	vk = vk_session.get_api()#проверка
	try:#если все норм то
		print(Fore.GREEN+'Aвторизация прошла успешно')
		massive = vk.groups.getMembers(group_id = id_pab, count = n)
		#print(massive['items'])
		print('Будет записано '+str(len(massive['items']))+' аккаунтов')#len - это длина массива . все взял str тк len() вернет число
		maksim_eblan(1)#это тип time.sleep(1)
		file = open("parser(id).txt", "w")#открытие файла на запись
		file2 = open("parser(links).txt", "w") # тоже самое что и с верху
		ids = massive['items']# передал значение словаря massive  items (а там массив с id)
		
		#print(ids)
		x=0
		for x in range(n):#цикл , который повторится 1к раз (у массива такая длина можно было for x in range(len(ids)) . Но нахуя если больше 1 к нельзя )
			file.write(str(ids[x])+'\n')#запись id 
			file2.write('vk.com/id'+str(ids[x])+'\n')#запись id  в формате vk.com/id1
			x+=1#
	
		print(Fore.GREEN+'готово))')
		
	except vk_api.exceptions.ApiError as error_msg:#если токен инвалид
		print(Fore.RED+'Данные недействительны')


def nakrutka(tk):
	token = tk#токен = переменной тк
	
	vk_session = vk_api.VkApi(token=token)#запрос авторизации
	vk = vk_session.get_api()#проверка
	try:#если все норм то
		print(Fore.GREEN+'Aвторизация прошла успешно')

		ids_file = open ('parser(id).txt','r',encoding='utf-8')#открытие на чтение

		ids_str = ids_file.readlines()#чтение всех линий и присваивание в переменную
		i = 0
		ids = [line.rstrip() for line in ids_str]

		while i < len(ids):
			try:
				vk.friends.add(user_id=int(ids[i]))
				print('заявка отправлена @id'+str(ids[i]))
				i+=1
				maksim_eblan(5)
			except vk_api.exceptions.Captcha :
				print('Капча ждем 5 мин')
				maksim_eblan(300)
	except vk_api.exceptions.ApiError as error_msg:#если токен инвалид
		print(Fore.RED+'Данные недействительны')

def main():#функция main хз зачем но я так люблю делать
	suka("clear")#очистка терминала
	print(Fore.GREEN+'[1]-парсер\n[2]-добавить в друзья(из файла parser(id).txt) ');o = str(input('[-->]')) # тут я через ; написал 2 строки (у меня на винде беда с колорамой можно было так : o = str(input(Fore.GREEN+'[1]-парсер\n[2]-добавить в друзья\n[-->]')))
	if o == '1':#проверка (сделал str так как пользователь может вместо числа написать строку  и будет ошибка , писанины больше будет . А так всегда строка )
		tk = str(input('ТОКЕН:'))#
		id_pab = int(input('id  паблика :'))#
		n = int(input('Сколько юзеров спарсить(не более 1000):'))#
		parser(tk=tk,id_pab=id_pab,n=n)#тут передаем в функцию парсера параметры и запускаем ее
	elif o == '2':
		tk = str(input('ТОКЕН:'))
		nakrutka(tk)
if __name__ == '__main__':#знаешь уже что это
	main()#вызов main