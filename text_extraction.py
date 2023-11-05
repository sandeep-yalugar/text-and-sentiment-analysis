from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time
import threading



df = pd.read_csv('blcInp.csv')

error_urls = []
def article(url,url_id,num):
  try:
    ht = requests.get(url).text
    soup = bs(ht,'lxml')
    div = soup.find('div',class_='td-post-content')
    h1 = soup.find('h1')
    title = h1.text
    arti = div.text
    if div==None or arti==None:
      print(f'error occuring in the thread {num} ')
      print(url)
    text = title + '.' + arti
    with open(f'{url_id}.txt','w') as fp:
      fp.write(text)


    
  except:
    global error_urls 
    print(url)
    error_urls.append(url)
