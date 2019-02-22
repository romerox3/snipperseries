# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib2,unicodedata, requests

def extractor(palabra):
    html = conector(palabra).text
    soup = BeautifulSoup(html)
    imgs = soup.findAll('img')
    urls = []

    for img in imgs:
    	urls.append(img['src'])

    return urls

def conector(palabra):
    try:
        conector = requests.get("https://www.google.com/search?q=" + palabra + "&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiinob3_KfgAhVKKBoKHUg9BqkQ_AUIDigB&biw=1853&bih=951")
        print(conector)
        return conector
    except:
        print("Tiempo de espera agotado, volviendo a intentar")

        # from bs4 import BeautifulSoup
        # import base64
        # import requests

        # session = requests.Session()
        # session.proxies = {'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9150'}

        # url = session.get("http://waeixxcraed4gw7q.onion/signin")
        # soup = BeautifulSoup(url.text, "lxml")
        # imgs = soup.findAll('img')

        # #save captcha from base64 encoding
        # img_data = bytes(imgs[1]['src'][23:],encoding='utf-8')
        # with open("olympus_captcha.jpg","wb") as fh:
        #     fh.write(base64.decodestring(img_data))

        # #solve the captcha that has been saved to the harddrive    
        # captcha = input("enter captcha:\n")

        # #attempt login (password and username removed)
        # payload = {"username":username, "password":password, "captcha":captcha}
        # response = session.post("http://waeixxcraed4gw7q.onion/signin", data = payload)
        # print(response.text)