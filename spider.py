
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import requests
import sqlite3

head = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43"
}

page_sum=input("呐，你想要几组色图呢？（笑）： ")
baseurl="https://wallhaven.cc/search?categories=010&purity=010&atleast=1920x1080&ratios=16x9&sorting=favorites&order=desc&page="
for page in range(0,int (page_sum),1):
    url=baseurl+str(page+1)
    request=urllib.request.Request(url,headers=head)
    response=urllib.request.urlopen(request)
    html=response.read().decode("utf-8")
    urls=re.findall('<a class="preview" href="(.*?)"',html)
    for i in range(24):
        x=(urls[i][23:])
        a=x[0]+x[1]
        UrlImg="https://w.wallhaven.cc/full/"+a+"/wallhaven-"+x+".jpg"
        code=requests.get(UrlImg).status_code
        if code ==404:
            UrlImg="https://w.wallhaven.cc/full/"+a+"/wallhaven-"+x+".png"
        urls[i]=UrlImg
        print(i+1,UrlImg)
        file_name=UrlImg.split('/')[-1]
        response=requests.get(UrlImg,headers=head)
        with open(file_name,"wb") as f:
            f.write(response.content)

os.system("pause")