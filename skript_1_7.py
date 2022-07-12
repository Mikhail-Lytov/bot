#skript_1.7
#code by Mikl
#version 1.4
from bs4 import BeautifulSoup
import requests
from outh_data import token
import time
import datetime

def pars_url(cnt_phot, group_name):
    url_list = []
    people_id = 183913151
    version = 5.131
    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count={cnt_phot}&access_token={token}&v={version}"
    req = requests.get(url)
    src = req.json()

    data_photos = src["response"]
    cnt_photos = data_photos["count"]
    items_photos = data_photos["items"]
    for item in range(cnt_phot):
            try:
                item_size = items_photos[item]["attachments"][0]["photo"]["sizes"]
            except Exception:
                t = 1
            if len(item_size) == 9:
                url = item_size[8]["url"]
            elif len(item_size) == 8:
                url = item_size[7]["url"]
            elif len(item_size) == 7:
                url = item_size[6]["url"]
            elif len(item_size) == 6:
                url = item_size[5]["url"]
            elif len(item_size) == 5:
                url = item_size[4]["url"]
            elif len(item_size) == 4:
                url = item_size[3]["url"]
            elif len(item_size) == 3:
                url = item_size[2]["url"]
            elif len(item_size) == 2:
                url = item_size[1]["url"]
            else:
                url = item_size[0]["url"]
            url_list.append(url)

    f = open("cat.txt" , "a")
    for i in range(cnt_phot):
        f.write(url_list[i] + '\n')
    f.close()

    
def main():
    f = open("cat.txt", 'w')
    f.close
    now = datetime.datetime.now() 
    print("Current date and time launching the parser: ") 
    print(now.strftime('%Y-%m-%d %H:%M:%S')) 
    print(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))

    print("Pars photos VK groups. Version 1.4")
    group_names = ['koshka_02', 'catmedicine','v.kote']#input("input group name: ") # готовые группы , 'pikhi_love'
    cnt_phot = 100 #int(input("input count photos: ")) #постоянную велич
    for item in group_names:
        group_name = item
        pars_url(cnt_phot, group_name)


if __name__ == '__main__':
    main()
