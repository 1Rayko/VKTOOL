import vk_api
import time 

def parser(url):
    # разраб - ленивая задница
    # и не хочет делать парсер шутОчек (17.10.2021)
    #https://pikabu.ru/story/anekdotyi__liker__7355548
    jokes = ["Почему парни инвалиды не смогут постоять за свою девушку?\nОни не смогут постоять за свою девушку",'У косоглазых людей, как правило две точки зрения','Как что делает наркоман, когда ему скучно?\nДурью мается','Альпинисты они как яйца, либо крутые, либо всмятку','Папа случайно проглотил флешку.\nТеперь он папка с файлами','У меня сломался туалет, позвонил сантехнику, а он мне говорит: не ссы, ща приеду','Интересный факт:\nУ безногого мужчины член до пола','Почему у инвалидов нет девушки?\nПотому что они подкатывают ко всем','Какую петлю сделал пилот - самоубийца?\nМертвую','Как остановить драку слепых?\nКрикнуть: я ставлю на того с ножом','Как называют автобус для перевозки Толстых людей?\nЖиробас','Как сделать так, чтобы секс перестал быть банальным?\nУбрать букву Б','В чем разница между печеньками и евреями?\nПеченьки достаются из печи'
]
    return jokes

def main(jokes):
    now=int(time.time())
      
    token = str(input("Token:"))
    f_o = int(input("Friends only?(1,0):"))
    if f_o == '' or ' ':
        f_o = 1

    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    
    for joke in jokes:
        vk.wall.post(
                friends_only=f_o,
                message=joke,
                publish_date=int(now)+3600
                )
        now+=3600
        print(joke)
        time.sleep(5)
jokes=parser(None)
main(jokes)
