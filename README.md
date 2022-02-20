# VKTOOL - CLI утилита для ВКонтакте

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=1Rayko&repo=VKTOOL&show_icons=true&theme=dark)](https://github.com/kotik06/VKTOOL)

## Установка

### Установка git
#### Arch Linux
```bash
sudo pacman -S git --noconfirm
```
#### Debian, Ubuntu
```bash
sudo apt-get install -y git
```
#### Void Linux
```bash
sudo xbps-install -S git
```
---
### Скачивание и установка Python3.10

#### Arch Linux
```bash
sudo pacman -Sy python python-pip
```
#### Void Linux
```bash
sudo xbps-install -S python3 python3-pip
```

### Установка PIP зависимостей
```bash
python3.10 -m pip install click vk_api Pillow
```
---
## Установка VKTOOL
### Клонирование репозитория
```bash
git clone https://github.com/1Rayko/VKTOOL 
```
### Запуск установщика
```bash
cd ~/VKTOOL && sudo python main.py install
```
---
## Запуск

### Полная версия
```bash
vktool-cli full
```
### Версия для накрутки фото
```bash
vktool-cli light
```
### Загрузка историй
```bash 
vktool-cli story
```
### "Шуточки"
```bash
vktool-cli one-jokes
```
---
## Обновления
### Вариант 1
```bash
sudo vktool-cli update
```
### Вариант 2 
```bash
cd ~/VKTOOL && git pull && sudo python main.py install
```
---
## Примеры использования
*Получить token можно на vkhost.github.io*
### Накрутка постов на стену
```bash
vktool-cli full
```
![Alt text](https://github.com/1Rayko/VKTOOL/blob/master/img/5.png)
![Alt text](https://github.com/1Rayko/VKTOOL/blob/master/img/6.png)

### Накрутка фото
```bash
vktool-cli light
```
![Alt text](https://github.com/1Rayko/VKTOOL/blob/master/img/7.png)
![Alt text](https://github.com/1Rayko/VKTOOL/blob/master/img/8.png)








