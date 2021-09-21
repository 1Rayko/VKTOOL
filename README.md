# VKTOOL


![Image](1.png)
![Image](2.png)
![Image](3.png)


## УСТАНОВКА:

### Устанавливаем системные зависимости
## Termux

```zsh
# Устанавливаем системные зависимости
pkg install git python3 python3-pip -y
```
## Ubuntu/Debian

```zsh
sudo apt install git python3 python3-pip -y
```

## Arch Linux

```zsh
sudo pacman -Sy git 
sudo pacman -Sy python
sudo pacman -Sy python-pip
```
### Клонируем репозиторий
```zsh
git clone https://github.com/kotik06/VKTOOL
```
### Установка питонячих библиотек + добавление алиаса в .bashrc, .zshrc
```zsh
cd VKTOOL && python main.py install
``` 
### Запуск
```zsh
#Запуск обычноый версии
vktool-cli full 

#Запуск лайт версии
vktool-cli light
```

### Обновления
```zsh
vktool-cli update
```
# Внимание: ![srakoeb2007](srakoeb2007.py) в бете! 
