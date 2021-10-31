# -*- coding: utf-8 -*-
import vk_api,os
from vk_api import VkUpload 
print("\033[36m"+ r"""
      _             _           
     | |           (_)          
  ___| |_ ___  _ __ _  ___  ___ 
 / __| __/ _ \| '__| |/ _ \/ __|
 \__ \ || (_) | |  | |  __/\__ \
 |___/\__\___/|_|  |_|\___||___/
(https://github.com/kotik06/VKTOOL)                                
        """+"\033[39m")
def main():
    token = input("Токен:").strip() 
    vk_session = vk_api.VkApi(token=token)
    try:
        
        upload = VkUpload(vk_session)
    except:
        print("Невалидный токен")
        main()
    path = input("Путь к файлу:").strip()
    type_ = input("Тип истории (photo или video):").strip() 
    upload.story(path,file_type=type_)

if __name__ == '__main__':
    main()
