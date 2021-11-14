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
---
### Скачивание и установка Python3.10

#### Arch Linux
```bash
git clone https://aur.archlinux.org/python310.git && cd python310 && makepkg -si
sudo ln -sf /usr/bin/python3.10 /usr/bin/python
```

#### Другие дистрибутивы
```bash
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz 
tar xzvf Python-3.10.0.tgz 
cd Python-3.10.0.tgz 
./configure --prefix=$HOME/python-3.10.0
make
make install
$HOME/python-3.10.0/bin/python3.10
sudo ln -sf /usr/bin/python3.10 /usr/bin/python
```
###### *PS. Следите за актуальными обновлениями вашего дистрибутива*
---
### Установка PIP
```bash
python3.10 -m ensurepip --default-pip
```
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
cd ~/VKTOOL && sudo python3.10 main.py install
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
vktool-cli update
```
### Вариант 2 
```bash
cd ~/VKTOOL && git pull
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








