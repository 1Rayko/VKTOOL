# VKTOOL - CLI утилита для ВКонтакте

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=1Rayko&repo=VKTOOL&show_icons=true&theme=dark)](https://github.com/kotik06/VKTOOL)

## Установка
### Установка системных зависимостей
#### Arch Linux
```bash
sudo pacman -S git python python-pip --noconfirm
```
#### Debian, Ubuntu
```bash
sudo apt-get install -y git python python-pip
```
#### Void Linux
```bash
sudo xbps-install -S git python3 python3-pip
```
---

## Установка VKTOOL
### Клонирование репозитория
```bash
git clone https://github.com/1Rayko/VKTOOL.git
```
### Запуск установщика
```bash
cd ~/VKTOOL && bash install
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
vktool-cli jokes
```
---
## Обновления
### Вариант 1
```bash
vktool-cli update
```
### Вариант 2 
```bash
cd ~/VKTOOL && git pull && bash install
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








