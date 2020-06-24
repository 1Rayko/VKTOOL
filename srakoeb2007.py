# -*- coding: utf-8 -*-
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
print('================================================\n================================================\n================================================\n              srakoeb2007\n================================================\n================================================\n================================================\n')
time.sleep(1)
menu='Выберите функцию:\n\n1.Запустить антикик и спам, если все последующие пункты проделаны\n2.Сгенерировать конфиг с токенами, загрузить текст из файла  "message.txt" и записать название беседы, которое поставят боты\n3.Зайти в конфу по ссылке\n4.Пригласить в конфу с главного акка\n5.Добавить друг друга в др\n6.Добавить пользователя в антикик\n7.Убрать пользователя из антикика\n8.Флуд в лс\n9.Сбросить каптчи на акках, если боты перестали флудить\n10.Записать айди рейд ботов\n11.Пригласить рейд ботов\n12.Узнать айди вк по домену\n13.Наш рейд бот для спама в конфах\n14.Исключить всех участников беседы\n15.Очистить группу вк от подпищиков\n16.Почистить стену вк\n17.Заспамить стену\n18.Заспамить комментарии\n19.Удаление всех комментариев\n20.Пригласить друзей со всех акков\n21.Автосмена паролей аккаунтов в acc.txt\n22.Разъеби вк другу\n23.Удалить спам в своей беседе\n24.Автоудаление сообщений свинок в беседе\n25.Ответ на сообщения говнотроллей\n26.Отправка сообщений от бота (группы вк)\n27.Антикик админки в группе\n28.Закинуть в чс всех друзей и подписчиков\n29.Удалить все подписки\n30.Разъебать коменты\n31.Засрать фотоальбом группы\n================================================\n\n'
while True:
	try:
		a=int(input(menu))
		if a == 1:
			class MyThread(Thread):
				def __init__(self, name):
					Thread.__init__(self)
					self.name = name
				def run(self):
					vk_session = vk_api.VkApi(token=self.name)
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type_id == VkChatEventType.USER_KICKED:
									requests.get("https://api.vk.com/method/messages.addChatUser?access_token="+self.name+"&v=5.92&chat_id="+str(event.chat_id)+"&user_id="+str(event.info['user_id']))
						except:
							pass
						print('Выйти из антикика вы сможете только закрыв окно с терминалом или нажав ctrl+c\nАктивировать спам можно командой '+info.info.call+' с акка любого бота\nЗапускается антикик...')
						time.sleep(1)
			class MyThread4(Thread):
				def __init__(self, name):
					Thread.__init__(self)
					self.name = name
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=info.info.captcha, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session = vk_api.VkApi(token=self.name, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in info.info.ids and event.text == info.info.call:
									while True:
										try:
											titled=vk.messages.getChat(chat_id=event.chat_id)['title']
											if titled == info.info.title:
												try:
													vk.messages.unpin(peer_id=event.peer_id)
												except:
													pass
												try:
													vk.messages.deleteChatPhoto(chat_id=event.chat_id)
												except:
													pass
												a=vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,message="Привет")
												vk.messages.edit(peer_id=event.peer_id,message=info.info.msg,message_id=a)
											if titled != info.info.title:
												a=vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,message="Петушары сосите")
												vk.messages.edit(peer_id=event.peer_id,message=info.info.msg,message_id=a)
												vk.messages.editChat(chat_id=event.chat_id,title=info.info.title)
												try:
													vk.messages.deleteChatPhoto(chat_id=event.chat_id)
												except:
													pass
												try:
													vk.messages.unpin(peer_id=event.peer_id)
												except:
													pass
										except:
											pass
						except:
							pass
			class MyThread6(Thread):
				def __init__(self, name,media):
					Thread.__init__(self)
					self.name = name
					self.media = media
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=info.info.captcha, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session = vk_api.VkApi(token=self.name, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in info.info.ids and event.text == info.info.call:
									while True:
										try:
											titled=vk.messages.getChat(chat_id=event.chat_id)['title']
											if titled == info.info.title:
												try:
													vk.messages.unpin(peer_id=event.peer_id)
												except:
													pass
												try:
													vk.messages.deleteChatPhoto(chat_id=event.chat_id)
												except:
													pass
												vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,attachment=media)
											if titled != info.info.title:
												vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,attachment=media)
												vk.messages.editChat(chat_id=event.chat_id,title=info.info.title)
												try:
													vk.messages.deleteChatPhoto(chat_id=event.chat_id)
												except:
													pass
												try:
													vk.messages.unpin(peer_id=event.peer_id)
												except:
													pass
										except:
											pass
						except:
							pass
			class MyThread3(Thread):
				def __init__(self, name):
					Thread.__init__(self)
					self.name = name
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=info.info.captcha, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session = vk_api.VkApi(token=self.name, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in info.info.ids and event.text == info.info.call:
									while True:
										try:
											a=vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,message="Петушары сосите")
											vk.messages.edit(peer_id=event.peer_id,message=info.info.msg,message_id=a)
										except:
											pass
						except:
							pass
			class MyThread5(Thread):
				def __init__(self, name,media):
					Thread.__init__(self)
					self.name = name
					self.media = media
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=info.info.captcha, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session = vk_api.VkApi(token=self.name, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in info.info.ids and event.text == info.info.call:
									while True:
										try:
											vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,attachment=media)
										except:
											pass
						except:
							pass

			choice=int(input('Выберите:\n1.Просто антикик\n2.Антикик+спам\n3.Антикик + спам + смена названия конфы\n4.Спам + смена названия\n5.Только спам!\n6.спам фото/видео\n7.спам фото/видео + антикик\n8.спам фото/видео + антикик + смена названия кф\n\n'))
			if choice == 1:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread(name)
					my_thread.start()
				else:
					time.sleep(1)
			if choice == 2:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread3(name)
					my_thread.start()
					my_thread = MyThread(name)
					my_thread.start()
				else:
					print('Антикик + спам запущен! Активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 3:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread4(name)
					my_thread.start()
					my_thread = MyThread(name)
					my_thread.start()
				else:
					print('Антикик + спам + смена названия запущены! Активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 4:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread4(name)
					my_thread.start()
				else:
					print('Спам + смена названия запущены! Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 5:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread3(name)
					my_thread.start()
				else:
					print('Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 6:
				media=input('Вставьте часть ссылки на фото или видео таким образом, как  в примере "photo123_45":\n')
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread5(name,media)
					my_thread.start()
				else:
					print('Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 7:
				media=input('Вставьте часть ссылки на фото или видео таким образом, как  в примере "photo123_45":\n')
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread5(name,media)
					my_thread.start()
					my_thread = MyThread(name)
					my_thread.start()
				else:
					print('Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 8:
				media=input('Вставьте часть ссылки на фото или видео таким образом, как  в примере "photo123_45":\n')
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread5(name,media)
					my_thread.start()
					my_thread = MyThread6(name,media)
					my_thread.start()
				else:
					print('Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
		if a == 2:
			b=int(input('Выберите, откуда будет прога брать данные:\n1.Номер + пароль в acc.txt\n2.Токены в token.txt\n\n'))
			if b == 1:
				try:
					print('Генерация конфига...')
					accs=len(open('acc.txt', 'r',encoding='utf8').readlines())
					k=open('info.py',"wt")
					k.write('class info():')
					k.close()
					print('генерация токенов и айди')
					tk=[]
					iddd=[]
					for x in range (accs):
						f=open('acc.txt',encoding='utf8').read()
						num_and_passwd=f.split('\n')[x]
						b=num_and_passwd.find(':')
						phone=num_and_passwd[:b]
						passwd=num_and_passwd[b+1:]
						try:
							f=requests.get("https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=%s" % str(phone) + "&password="+str(passwd))
							tk.append(str(f.json()["access_token"]))
							iddd.append(str(f.json()["user_id"]))
						except:
							print("Акк в файле 'acc.txt', строка "+str(x+1)+" невалид")
							pass
					k=open('info.py',"at",encoding='utf8')
					k.write('\n	tokenlist ='+str(tk)+'\n	ids='+str(iddd))
					k.close()
					print("установка сообщения")
					text1=open('message.txt',"rt",encoding='utf8').read().strip("\n")
					a=open('info.py',"at",encoding='utf8')
					a.write("\n	msg='"+text1+"'\n	title='"+input('Сообщение для спама у вас теперь обновлено в файле "message.txt". Введите название беседы, какое будет при рейде: ')+"'\n	captcha='"+input('Ключ от "https://anti-captcha.com/": ')+"'\n	call='"+input("Введите боевой клич, на который рейд боты начнут спамить: ")+"'")
					a.close()
					try:
						importlib.reload(info)
						print('Готово! Данные обновлены!')
					except:
						print('Готово! Данные обновлены! НО НУЖНО ПЕРЕЗАПУСТИТЬ ПРОГУ')
						pass
					time.sleep(1)
				except:
					print('\nВы неправильно ввели данные')
					time.sleep(1)
			if b == 2:
				try:
					print('Генерация конфига...')
					k=open('info.py',"wt",encoding='utf8')
					k.write('class info():')
					k.close()
					print('генерация айди')
					accs=len(open('token.txt', 'r',encoding='utf8').readlines())
					tk=[]
					iddd=[]
					for x in range (accs):
						f=open('token.txt',encoding='utf8').read()
						token=f.split('\n')[x]
						try:
							f=requests.get("https://api.vk.com/method/users.get?access_token="+token+"&v=5.92")
							iddd.append(str(f.json()["response"][0]['id']))
							tk.append(token)
						except:
							print("Акк в файле 'acc.txt', строка "+str(x+1)+" невалид")
							pass
					print('ввод токенов')
					k=open('info.py',"at",encoding='utf8')
					k.write('\n	tokenlist ='+str(tk)+'\n	ids='+str(iddd)+'\n')
					k.close()
					print("установка сообщения")
					k=open('info.py',"rt",encoding='utf8').read()
					text=k[0:len(k)-1]
					text1=open('message.txt',"rt",encoding='utf8').read().strip("\n")
					a=open('info.py',"wt",encoding='utf8')
					a.write(text+"\n	msg='"+text1+"'\n	title='"+input('Сообщение для спама у вас теперь обновлено в файле "message.txt". Введите название беседы, какое будет при рейде: ')+"'\n	captcha='"+input('Ключ от "https://anti-captcha.com/": ')+"'\n	call='"+input("Введите боевой клич, на который рейд боты начнут спамить: ")+"'")
					a.close()
					try:
						importlib.reload(info)
						print('Готово! Данные обновлены!')
					except:
						print('Готово! Данные обновлены! НО НУЖНО ПЕРЕЗАПУСТИТЬ ПРОГУ')
						pass
					time.sleep(1)
				except Exception as e:
					print('Ошибка:\n', traceback.format_exc())
					print('\nВы неправильно ввели данные')
					time.sleep(1)
		if a == 3:
			link=input('Ссылка на беседу: ')
			print('Заход в конфу...')
			for user in info.info.tokenlist:
				requests.get("https://api.vk.com/method/messages.joinChatByInviteLink?access_token="+user+"&v=5.92&link="+link)
			else:
				print('Все зашли!')
		if a == 4:
			print('Главный акк - ваш аккаунт, с которого вам надо пригласить всех в конфу\nУказывайте его логин и пароль в первой строке')
			owner=info.info.tokenlist[0]
			chat=input('введите айди беседы: ')
			print('Запуск')
			for acc in info.info.ids:
				requests.get("https://api.vk.com/method/messages.addChatUser?access_token="+owner+"&v=5.92&chat_id="+chat+"&user_id="+acc)
			else:
				print('Все приглашены!')
		if a == 5:
			class MyThread2(Thread):
				def __init__(self, name,captcha_key):
					Thread.__init__(self)
					self.name = name
					self.captcha_key = captcha_key
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=self.captcha_key, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					token=self.name
					vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					a=requests.get("https://api.vk.com/method/users.get?access_token="+self.name+"&v=5.92").json()
					name=a['response'][0]['first_name']
					surname=a['response'][0]['last_name']
					print(name+" "+surname+" добавляет в друзья")
					for idd in info.info.ids:
						try:
							vk.friends.add(user_id=idd)
						except:
							pass
					else:
						print(name+" "+surname+" добавил в друзья!")
			captcha_key=info.info.captcha
			for x in range(len(info.info.tokenlist)):
				name = info.info.tokenlist[x]
				my_thread = MyThread2(name,captcha_key)
				my_thread.start()
			time.sleep(5)
		if a == 6:
			captcha_key=info.info.captcha
			iduser=input('Айди пользователя, которого вы хотите добавить в антикик: ')
			for token in info.info.tokenlist:
				def captcha_handler(captcha):
					key = ImageToTextTask.ImageToTextTask(anticaptcha_key=captcha_key, save_format='const') \
							.captcha_handler(captcha_link=captcha.get_url())
					return captcha.try_again(key['solution']['text'])
				try:
					vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					vk.friends.add(user_id=iduser)
				except:
					pass
			else:
				print('Пользователю отправлены заявки друзья. Когда он их примит, он будет добавлен в антикик')
		if a == 7:
			iduser=input('Айди пользователя, которого вы хотите убрать из антикика: ')
			for token in info.info.tokenlist:
				requests.get("https://api.vk.com/method/friends.delete?access_token="+token+"&v=5.92&user_id="+iduser)
			else:
				print('Пользователь убран из антикика')
		if a == 8:
			class ls(Thread):
				def __init__(self, name,iduser,media):
					Thread.__init__(self)
					self.name = name
					self.iduser = iduser
					self.media = media
				def run(self):
					token=self.name
					x=100
					while x > 0:
						c=len(info.info.tokenlist)
						while c > 0:
							try:
								vk_session = vk_api.VkApi(token=token)
								vk = vk_session.get_api()
								vk.messages.send(user_id=self.iduser,message=info.info.msg,attachment=self.media,random_id=random.randint(100000,999999))
							except:
								pass
							c-=1
						x-=1
			iduser=input('Айди того, кому надо засрать лс: ')
			media=input('Введите ссылку на медиафайл, например "photo459509306_457244578". Если вам не нужно прикреплять медиафайл, то пропустите, нажав enter: ')
			for x in range(len(info.info.tokenlist)):
				name = info.info.tokenlist[x]
				my_thread = ls(name,iduser,media)
				my_thread.start()
		if a == 9:
			captcha_key=info.info.captcha
			for x in range (len(info.info.tokenlist)):
				def captcha_handler(captcha):
					key = ImageToTextTask.ImageToTextTask(anticaptcha_key=captcha_key, save_format='const') \
							.captcha_handler(captcha_link=captcha.get_url())
					return captcha.try_again(key['solution']['text'])
				try:
					token=info.info.tokenlist[x]
					iduser=info.info.ids[x]
					vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					vk.messages.send(user_id=iduser,message=".",random_id=random.randint(100000,999999))
					vk.messages.editChat(chat_id=1,title=".",random_id=random.randint(100000,999999))
				except:
					pass
			else:
				print('Акки очищены от каптч!')
		if a == 10:
			try:
				a=open('pod.py',"wt",encoding='utf8')
				a.write("class pod():\n	idbots=["+input("Запишите айди групп через запятую с минусом:\n")+"]")
				a.close()
				try:
					importlib.reload(pod)
					print('Токен добавлен и id записаны!')
				except:
					print('Токен добавлен и id записаны! НО НУЖНО ПЕРЕЗАПУСТИТЬ ПРОГУ')
					pass
			except:
				print("Вы неправильно вставили данные")
			time.sleep(1)
		if a == 11:
			print('Чтобы получить токен для инвайта рейд ботов да и других ботов, вам нужно перейти по ссылке\nhttps://oauth.vk.com/authorize?client_id=6441755&redirect_uri=https://api.vk.com/blank.html&display=page&response_type=token&revoke=1\nИ подтвердить. А потом вставить новый токен, который сгенерировался в браузере')
			token=input("Вставьте токен из новой ссылки, он начинается от 'access_token=' и заканчивается до '&expires_in': ")
			idconf=str(2000000000+int(input('Введите айди беседы для приглашения ботов: ')))
			print("Приглашение ботов в беседу")
			try:
				for x in pod.pod.idbots:
					requests.get("https://api.vk.com/method/bot.addBotToChat?access_token="+token+"&peer_id="+idconf+"&bot_id="+str(x)+"&v=5.92")
				else:
					print("Боты приглашены!")
			except:
				print("Заполните конфигурацию для приглашения в пункте 10")
			time.sleep(1)
		if a == 12:
			link=input("Введите домен группы или страницы:\n")
			try:
				idvk=requests.get("https://api.vk.com/method/utils.resolveScreenName?access_token="+info.info.tokenlist[0]+"&screen_name="+link+"&v=5.92").json()['response']['object_id']
				print('Айди -',idvk)
				time.sleep(5)
			except:
				print("Такого домена нету")
				time.sleep(5)
		if a == 13:
			print('У нас есть свой рейд бот. Он платный, но плата даёт вам возможность получить быстрый спам от 900 сообщений и до больше тысячи\nhttps://t.me/bot_drochila - ссылка на него')
			time.sleep(5)
		if a == 14:
			b=int(input("1.Удалить пользователем конфу\n2.Удалить конфу группой\n\n"))
			if b == 1:
				print('Главный акк - ваш аккаунт, с которого вам надо кикнуть всех участников в беседе\nУказывайте его логин и пароль в первой строке')
				owner=info.info.tokenlist[0]
				chat=input('введите айди беседы: ')
				a=requests.get("https://api.vk.com/method/messages.getChat?access_token="+owner+"&chat_id="+chat+"&v=5.92").json()['response']['users']
				print('Запуск')
				for i in a:
					if not str(i) in info.info.ids:
						requests.get("https://api.vk.com/method/messages.removeChatUser?access_token="+owner+"&chat_id="+chat+"&member_id="+str(i)+"&v=5.92")
			if b == 2:
				idgroup=input('Введите айди группы без минуса:\n')
				tokengroup=input('Перейдите по этой ссылке:\n\nhttps://oauth.vk.com/authorize?client_id=3116505&scope=messages,manage,photos,docs,wall,stories&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&group_ids='+idgroup+'\n\nИ нажмите "разрешить" и вставьте текст после "&access_token_'+idgroup+'=" :\n')
				vk_session = vk_api.VkApi(token=tokengroup)
				vk = vk_session.get_api()
				print('Пригласите бота в беседу и отправьте ему упоминание')
				try:
					longpoll = VkBotLongPoll(vk_session, int(idgroup))
				except:
					print('При ошибке зайдите сюда - https://vk.com/club'+idgroup+'?act=longpoll_api\nВключите там Long Poll API и постаавьте версию 5.85\nПотом в https://vk.com/club'+idgroup+'?act=longpoll_api_types поставьте\nпоставьте галочку на "Входящее сообщение"')
				for event in longpoll.listen():
					if event.type == VkBotEventType.MESSAGE_NEW:
						print('Айди беседы - ',event.chat_id)
						idkf=event.chat_id
						break
				count=len(requests.get("https://api.vk.com/method/messages.getConversationMembers?access_token="+tokengroup+"&v=5.92&peer_id=%s" % str(2000000000+idkf)).json()['response']['items'])
				print('Закрыть программу и писать потом в новую конфу можно, только нужно закрыть окно\n')
				c=int(input('В беседе '+str(count)+' участников. Кикнуть их?\n1.Да\n2.Нет\n\n'))
				if c == 1:
					idishnik=requests.get("https://api.vk.com/method/messages.getConversationMembers?access_token="+tokengroup+"&v=5.92&peer_id=%s" % str(2000000000+idkf)).json()['response']['items']
					for x in range(count):
						if not str(idishnik[x]['member_id']) in info.info.ids and str(idishnik[x]['member_id']) != "-"+idgroup:
							requests.get("https://api.vk.com/method/messages.removeChatUser?access_token=%s" % tokengroup+"&v=5.92&chat_id="+str(idkf)+"&member_id="+str(idishnik[x]['member_id']))
				if c == 2:
					pass
		if a == 15:
			token=info.info.tokenlist[0]
			group_id=input('Айди группы без минуса: ')

			class MyThread11(Thread):
				def __init__(self, i):
					Thread.__init__(self)
					self.i = i
				def run(self):
					print("Удалён "+str(self.i))
					requests.get("https://api.vk.com/method/groups.removeUser?access_token="+token+"&group_id="+group_id+"&user_id="+str(self.i)+"&v=5.92").json()
			while True:
				a=requests.get("https://api.vk.com/method/groups.getMembers?access_token="+token+"&group_id="+group_id+"&v=5.92").json()['response']['items']
				for i in a:
					try:
						my_thread = MyThread11(i)
						my_thread.start()
					except:
						pass
		if a == 16:
			class MyThread12(Thread):
				def __init__(self, x,owner,token):
					Thread.__init__(self)
					self.x = x
					self.owner = owner
					self.token = token
				def run(self):
					requests.get("https://api.vk.com/method/wall.delete?access_token=%s" % str(token)+"&owner_id="+str(owner)+"&post_id="+str(x)+"&v=5.92")
			token=info.info.tokenlist[0]
			owner=input("Айди страницы (без минуса) или айди группы с минусом, чтобы всё удалить: \n")
			a=requests.get("https://api.vk.com/method/wall.get?access_token=%s" % str(token)+"&owner_id="+str(owner)+"&count=1&v=5.92").json()['response']['items'][0]['id']
			for x in sorted(list(range(a+1)), reverse = True):
				print("Удалён пост - wall"+str(owner)+str("_")+str(x))
				my_thread = MyThread12(x,token,owner)
				my_thread.start()
				time.sleep(0.5)
			else:
				print("Всё удалено!")
				pass
		if a == 17:
			class MyThread13(Thread):
				def __init__(self,x,wall):
					Thread.__init__(self)
					self.x = x
					self.wall = wall
				def run(self):
					vk_session = vk_api.VkApi(token=self.x)
					vk = vk_session.get_api()
					vk.wall.post(owner_id=wall,message='че костя еблоид угрожать мне думал 2дшный уебок пошел нахуй', attachments = 'photo313659956_457246080')
			wall=input("Айди страницы (без минуса) или айди группы с минусом, чтобы заспамить: \n")
			print('Спам начался!')
			for x in info.info.tokenlist:
				for a in range(10):
					my_thread = MyThread13(x,wall)
					my_thread.start()
					time.sleep(1)
			else:
				print('Спам завершился!')
		if a == 18:
			class MyThread14(Thread):
				def __init__(self,x,wall,idpost, attach):
					Thread.__init__(self)
					self.x = x
					self.wall = wall
					self.idpost = idpost
					self.attach = attach
				def run(self):
					vk_session = vk_api.VkApi(token=self.x)
					vk = vk_session.get_api()
					vk.wall.createComment(owner_id=wall,post_id=idpost, attachments = self.attach, message = 'я твою мать на базаре продал, плагиат поста обоссаный')
			wall=input("Айди страницы (без минуса) или айди группы с минусом, чтобы заспамить: \n")
			idpost=input("Айди поста (находится в ссылке на пост после _ \n")
			attach = input('Аттачи: ')
			print('Спам начался в комментарии!')
			for x in info.info.tokenlist:
				for a in range(10):
					my_thread = MyThread14(x,wall,idpost, attach)
					my_thread.start()
					time.sleep(1)
			else:
				print('Спам завершился!')
		if a == 19:
			token=info.info.tokenlist[0]
			owner=input("Айди страницы (без минуса) или айди группы с минусом, чтобы удалить комментарии: \n")
			idpost=input("Айди поста (находится в ссылке на пост после _ \n")
			count=requests.get("https://api.vk.com/method/wall.getComments?access_token=%s" % str(token)+"&owner_id="+str(owner)+"&post_id="+idpost+"&count=1&v=5.92").json()['response']['count']
			print(count)
			for x in range(int(count)):
				a=requests.get("https://api.vk.com/method/wall.getComments?access_token=%s" % str(token)+"&owner_id="+str(owner)+"&post_id="+idpost+"&count=1&v=5.92").json()['response']['items'][0]['id']
				print("Удалён",x+1,"комментарий")
				requests.get("https://api.vk.com/method/wall.deleteComment?access_token=%s" % str(token)+"&owner_id="+str(owner)+"&comment_id="+str(a)+"&v=5.92")
				time.sleep(0.5)
			else:
				print("Комментарии удалены!")
				pass
		if a == 20:
			class MyThread16(Thread):
				def __init__(self,x):
					Thread.__init__(self)
					self.x = x
				def run(self):
					token=info.info.tokenlist[self.x]
					idi=info.info.ids[self.x]
					vk_session = vk_api.VkApi(token=token)
					vk = vk_session.get_api()
					longpoll = VkLongPoll(vk_session)
					for event in longpoll.listen():
						if event.type == VkEventType.MESSAGE_NEW and event.text == "invite":
							a=requests.get("https://api.vk.com/method/friends.get?access_token="+token+"&user_id="+str(idi)+"&v=5.92").json()['response']['items']
							print('Приглашение началось c',self.x+1,'акка')
							for i in a:
								requests.get("https://api.vk.com/method/messages.addChatUser?access_token="+token+"&chat_id="+str(event.chat_id)+"&user_id="+str(i)+"&v=5.92")
							else:
								print('Все друзья приглашены с',self.x,' акка!')
			print('Чтобы всё активировать, напишите в беседе команду "invite"')
			time.sleep(3)
			for x in range(len(info.info.tokenlist)):
				my_thread = MyThread16(x)
				my_thread.start()
		if a == 21:
			newparol=input("Перед тем, как менять пароли на купленных акках, выполните пункт 2 в меню\nНовый пароль для аккаунтов:\n")
			print("Смена паролей началась:\n")
			for x in range(len(info.info.tokenlist)):
				try:
					token=info.info.tokenlist[x]
					print("Смена пароля на "+str(x+1)+" акке")
					f=open('acc.txt').read()
					num_and_passwd=f.split('\n')[x]
					b=num_and_passwd.find(':')
					passwd=num_and_passwd[b+1:len(num_and_passwd)]
					a=requests.get("https://api.vk.com/method/account.changePassword?access_token=%s" % str(token)+"&old_password="+str(passwd)+"&new_password="+newparol+"&v=5.92").json()['response']
					print(a)
					time.sleep(1)
				except:
					print(str(x+1)+" пароль не сменен")
					pass
			else:
				print("Смена паролей звершена! Осталось только в acc.txt все старые пароли заменить на 1 новый, который вы написали!")
		if a == 22:
			print('Вы сможете разъебать лс друга, тем, что автоматом создадите 5 бесед и туда, тоже автоматом, инвайтните рейд бота. От этого зависает всё')
			class prik(Thread):
				def __init__(self,tknls,tknnv,gr,idfr,captcha_key,your_id):
					Thread.__init__(self)
					self.tknls = tknls
					self.tknnv = tknnv
					self.gr = gr
					self.idfr = idfr
					self.captcha_key = captcha_key
					self.your_id = your_id
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=self.captcha_key, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session11 = vk_api.VkApi(token=self.tknls, captcha_handler=captcha_handler)
					vk11 = vk_session11.get_api()
					kflist=[]
					try:
						for x in range(5):
							idkf=vk11.messages.createChat(user_ids=self.idfr,title=str(x+1))
							kflist.append(idkf)
						for idkf in kflist:
							requests.get("https://api.vk.com/method/bot.addBotToChat?access_token="+self.tknnv+"&peer_id="+str(2000000000+int(idkf))+"&bot_id=-"+self.gr+"&v=5.92")
							requests.get("https://api.vk.com/method/messages.removeChatUser?access_token="+self.tknls+"&chat_id="+str(idkf)+"&user_id="+self.your_id+"&v=5.92")
						print('Всё работает. Пизда другу')
					except:
						pass
			captcha_key=info.info.captcha
			text=input('Прикол с созданием бесед. Вам нужно отправить команду - "<1токен>,<2токен>,<айди рейд бота без минуса>,<айди друга>,<айди своей страницы>".\n 1 токен получается по ссылке - https://oauth.vk.com/authorize?client_id=2685278&scope=notify%2Cphotos%2Cfriends%2Caudio%2Cvideo%2Cnotes%2Cpages%2Cdocs%2Cstatus%2Cquestions%2Coffers%2Cwall%2Cgroups%2Cmessages%2Cnotifications%2Cstats%2Cads%2Coffline&redirect_uri=https://api.vk.com/blank.html&display=page&response_type=token&revoke=1\n2 токен получается по ссылке -\nhttps://oauth.vk.com/authorize?client_id=6441755&redirect_uri=https://api.vk.com/blank.html&display=page&response_type=token&revoke=1\nПример команды - \n13d53d4d16478bbf7bcd3f197056483b43a6a41dcf87d629cf14d72a7fa5673b5e75dd72cd233b23616f11,3d53d4d16478bbf7bcd3f197056483b43a6a41dcf87d629cf14d72a7fa5673b5e75dd72cd233b23616f11,187992544,567212524\n')
			infolist=text.split(',')
			tknls=infolist[0]
			tknnv=infolist[1]
			gr=infolist[2]
			idfr=infolist[3]
			your_id=infolist[4]
			my_thread = prik(tknls,tknnv,gr,idfr,captcha_key,your_id)
			my_thread.start()
		if a == 23:
			print('Действие выполняется с главного (первого акка)')
			class delraid(Thread):
				def __init__(self,idkf):
					Thread.__init__(self)
					self.idkf = idkf
				def run(self):
					while True:
						a=requests.get("https://api.vk.com/method/messages.getHistory?access_token="+info.info.tokenlist[0]+"&peer_id="+str(2000000000+int(self.idkf))+"&count=200&v=5.92").json()
						print('Идёт удаление 200 соообщений последних')
						for x in range(200):
							try:
								requests.get("https://api.vk.com/method/messages.delete?access_token="+info.info.tokenlist[0]+"&message_ids="+str(a['response']['items'][x]['id'])+"&delete_for_all=true&v=5.92")
							except:
								pass
			idkf=input('Введите айди беседы:\n')
			my_thread = delraid(idkf)
			my_thread.start()
			print('Удаление началось')
		if a == 24:
			print('Действие выполняется с главного (первого акка)')
			class delsvin(Thread):
				def __init__(self,idvk):
					Thread.__init__(self)
					self.idvk = idvk
				def run(self):
					idvklist=self.idvk.split(',')
					vk_session = vk_api.VkApi(token=info.info.tokenlist[0])
					vk = vk_session.get_api()
					while True:
						try:
							longpoll = VkLongPoll(vk_session)
							for event in longpoll.listen():
								if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in idvklist:
									try:
										vk.messages.delete(message_ids=event.message_id,delete_for_all='true')
									except:
										vk.messages.delete(message_ids=event.message_id)
									print(event.text)
						except:
							pass
			idvk=input('Чтобы поставить на автоудаление, введите айди вк у свиньи. Если вк свинов, то введите их через запятую:\n')
			my_thread = delsvin(idvk)
			my_thread.start()
		if a == 25:
			print('Действие выполняется с главного акка (первая строка в acc или token txt)')
			g=input("1.Просто ответ\n2.Ответ с пересыланием\n\n")
			class answer(Thread):
				def __init__(self,idvk,anticaptcha,msg,media,g):
					Thread.__init__(self)
					self.idvk = idvk
					self.anticaptcha = anticaptcha
					self.msg = msg
					self.media = media
					self.g = g
				def run(self):
					idvklist=self.idvk.split(',')
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=self.anticaptcha, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session = vk_api.VkApi(token=info.info.tokenlist[0], captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					if self.g == "1":
						while True:
							try:
								longpoll = VkLongPoll(vk_session)
								for event in longpoll.listen():
									if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in idvklist:
										vk.messages.send(peer_id=event.peer_id,message=self.msg,attachment=self.media,random_id=random.randint(0,999999))
										break
							except:
								pass
					if self.g == "2":
						while True:
							try:
								longpoll = VkLongPoll(vk_session)
								for event in longpoll.listen():
									if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in idvklist:
										vk.messages.send(peer_id=event.peer_id,message=self.msg,attachment=self.media,random_id=random.randint(0,999999),reply_to=event.message_id)
										break
							except:
								pass
			anticaptcha=info.info.captcha
			idvk=input('Чтобы поставить автоответчик на троля тупого, введите его или их айди через запятую:\n')
			msg=input('Введите аргумент на свина:\n')
			media=input('Введите ссылку на медиафайл, например "photo459509306_457244578". Если вам не нужно прикреплять медиафайл, то пропустите, нажав enter: ')
			my_thread = answer(idvk,anticaptcha,msg,media,g)
			my_thread.start()
		if a == 26:
			idgroup=input('Введите айди группы без минуса:\n')
			tokengroup=input('Перейдите по этой ссылке:\n\nhttps://oauth.vk.com/authorize?client_id=3116505&scope=messages,manage,photos,docs,wall,stories&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&group_ids='+idgroup+'\n\nИ нажмите "разрешить" и вставьте текст после "&access_token_'+idgroup+'=" :\n')
			vk_session = vk_api.VkApi(token=tokengroup)
			vk = vk_session.get_api()
			print('Пригласите бота в беседу и отправьте ему упоминание')
			try:
				longpoll = VkBotLongPoll(vk_session, int(idgroup))
			except:
				print('При ошибке зайдите сюда - https://vk.com/club'+idgroup+'?act=longpoll_api\nВключите там Long Poll API и постаавьте версию 5.85\nПотом в https://vk.com/club'+idgroup+'?act=longpoll_api_types поставьте\nпоставьте галочку на "Входящее сообщение"')
			for event in longpoll.listen():
				if event.type == VkBotEventType.MESSAGE_NEW:
					print('Айди беседы - ',event.chat_id)
					idkf=event.chat_id
					break
			while True:
				try:
					print('Закрыть программу и писать потом в новую конфу можно, закрыв окно\n')
					b=input("1.Отправка тектовых сообщений\n2.Отправка сообщения с картинками, постами и др медиа\n3.Отправка голосовых\n\n")
					b=int(b)
					if b==1:
						msg=input('Введите сообщение для отправки:\n')
						vk.messages.setActivity(peer_id=2000000000+int(idkf),type="typing")
						vk.messages.send(chat_id=idkf,random_id=random.randint(100000,999999),message=msg)
					if b==2:
						msg=input('Введите сообщение для отправки:\n')
						media=input('Введите ссылку на медиафайл. Например,\nфото:photo569032579_457239254\nвидео:video-143621955_456239085\nпоста:wall-143621955_9850\n')
						vk.messages.setActivity(peer_id=2000000000+int(idkf),type="typing")
						vk.messages.send(chat_id=idkf,random_id=random.randint(100000,999999),message=msg,attachment=media)
					if b==3:
						msg=input('Введите сообщение для отправки:\n')
						user=int(idkf)+2000000000
						a=vk.docs.getMessagesUploadServer(type='audio_message',peer_id=user)['upload_url']
						file=input('ссылка на запись: ')
						img = {'file': ('a.ogg', open((file), 'rb'))}
						response = requests.post(a, files=img)
						result = json.loads(response.text)['file']
						owner=vk.docs.save(file=result)['audio_message']['owner_id']
						document=vk.docs.save(file=result)['audio_message']['id']
						send = 'doc'+str(owner)+'_'+str(document)
						vk.messages.setActivity(peer_id=user,type="audiomessage")
						vk.messages.send(chat_id=idkf,random_id=random.randint(100000,999999),message=msg,attachment=send)
				except:
					pass
		if a == 27:
			idgroup=input("Введите айди группы:\n")
			print('''Не забудьте по ссылке (https://vk.com/club'''+idgroup+'''?act=longpoll_api_types) поставить галочку на смену руководства в разделе "прочее" ''')
			tokengroup=input('Перейдите по этой ссылке:\n\nhttps://oauth.vk.com/authorize?client_id=3116505&scope=messages,manage,photos,docs,wall,stories&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&group_ids='+idgroup+'\n\nИ нажмите "разрешить" и вставьте текст после "&access_token_'+idgroup+'=" :\n')
			vk_session = vk_api.VkApi(token=tokengroup)
			vk = vk_session.get_api()
			try:
				longpoll = VkBotLongPoll(vk_session, int(idgroup))
			except:
				print('При ошибке зайдите сюда - https://vk.com/club'+idgroup+'?act=longpoll_api\nВключите там Long Poll API и постаавьте версию 5.85\nПотом в https://vk.com/club'+idgroup+'?act=longpoll_api_types поставьте\nпоставьте галочку на "Входящее сообщение"')
			while True:
				for event in longpoll.listen():
					if event.type == VkBotEventType.GROUP_OFFICERS_EDIT and str(event.object.user_id) in info.info.ids:
						print(event.object.user_id)
						requests.get("https://api.vk.com/method/groups.editManager?access_token="+info.info.tokenlist[0]+"&group_id="+idgroup+"&user_id="+str(event.object.user_id)+"&v=5.92&role=administrator")
						print("Попытка исключить была проведена")
		if a == 28:
			token=input("Введите токен пользователя: ")
			idvk=requests.get("https://api.vk.com/method/users.get?access_token="+token+"&v=5.92").json()["response"][0]['id']
			friends=requests.get("https://api.vk.com/method/friends.get?access_token="+token+"&user_id="+str(idvk)+"&v=5.92").json()["response"]["items"]
			subs=requests.get("https://api.vk.com/method/users.getFollowers?access_token="+token+"&user_id="+str(idvk)+"&v=5.92&count=1000").json()["response"]["items"]
			for loh in subs:
				requests.get("https://api.vk.com/method/account.ban?access_token="+token+"&owner_id="+str(loh)+"&v=5.92")
			for loh in friends:
				requests.get("https://api.vk.com/method/account.ban?access_token="+token+"&owner_id="+str(loh)+"&v=5.92")
		if a == 29:
			token=input("Введите токен пользователя: ")
			idvk=requests.get("https://api.vk.com/method/users.get?access_token="+token+"&v=5.92").json()["response"][0]['id']
			groups=requests.get("https://api.vk.com/method/groups.get?access_token="+token+"&user_id="+str(idvk)+"&v=5.92").json()["response"]["items"]
			for loh in groups:
				requests.get("https://api.vk.com/method/groups.leave?access_token="+token+"&group_id="+str(loh)+"&v=5.92")
		if a == 30:
			ag="Срачевня активирована!"
			class ha(Thread):
				def __init__(self,ag,token,y,svini):
					Thread.__init__(self)
					self.ag = ag
					self.token = token
					self.y = y
					self.svini = svini
				def run(self):
					f=open("upd.txt","wt",encoding='utf8')
					f.write("1")
					f.close()
					print(self.ag)
					while True:
						try:
							a=open("args.txt",encoding='utf8')
							info=a.read().split("\n")
							a.close()
							k1=self.y.find("_")
							idstore=self.y[4:k1]
							k2=self.y.find("?")
							idpost=self.y[k1+1:k2]
							thr=self.y[k2+7:]
							a = requests.get("https://api.vk.com/method/wall.getComments?access_token=" + self.token+"&owner_id="+idstore+"&post_id="+idpost+"&count=1&sort=desc&comment_id="+thr+"&v=5.92").json()
							update = a['response']['items'][0]['id']
							who=a['response']['items'][0]['from_id']
							readd=open("upd.txt",encoding='utf8')
							upd=readd.read().strip("'b")
							readd.close()
							if str(who) in self.svini and  update != str(upd):
								f=open("upd.txt","wt",encoding='utf8')
								f.write(str(update))
								f.close()
								time.sleep(random.randint(3,9))
								msg=info[random.randint(0,len(info))]
								requests.get("https://api.vk.com/method/wall.createComment?access_token="+self.token+"&v=5.92&owner_id="+idstore+"&post_id="+idpost+"&reply_to_comment="+str(update)+"&message="+msg)
						except:
							pass
			token=info.info.tokenlist[0]
			print("Внимание! Сообщение отправляются от того акка, который первый по списку в acc.txt или token.txt")
			y=input('Ссылка на коментарий, под которым идёт срач, например "wall-77751588_10845?reply=11186" без кавычек: ')
			svini=input('Айди свинок через запятую: ').split(",")
			arg = ha(ag,token,y,svini)
			arg.start()
			time.sleep(3)
		if a == 31:
			class photos(Thread):
				def __init__(self,token,group_id,album_id,photo):
					Thread.__init__(self)
					self.token = token
					self.group_id = group_id
					self.album_id = album_id
					self.photo = photo
				def run(self):
					a=requests.get("https://api.vk.com/method/photos.getUploadServer?access_token="+self.token+"&v=5.92&album_id="+self.album_id+"&group_id="+self.group_id).json()['response']['upload_url']
					img = {'photo': ('ha.jpg', open(self.photo, 'rb'))}
					response = requests.post(a, files=img).json()
					print(response)
					while True:
						requests.get("https://api.vk.com/method/photos.save?access_token="+self.token+"&v=5.92&album_id="+self.album_id+"&group_id="+self.group_id+"&server="+str(response['server'])+'&photos_list='+str(response['photos_list'])+'&hash='+str(response['hash']))
			token=info.info.tokenlist[0]
			print("Внимание! Фото отправляются от того акка, который первый по списку в acc.txt или token.txt")
			group_id =input("Айди группы: ")
			album_id =input("Айди альбома: ")
			photo = input("Вставьте полную ссылку на фото, например, C:\\Users\\VasyaDolmat\\Pictures\\a.png: ").strip('"')
			print('Фото загружено. Началось засерание!')
			photo1 = photos(token,group_id,album_id,photo)
			photo1.start()
	except Exception as e:
		print('Ошибка:\n', traceback.format_exc())
		break
