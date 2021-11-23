
from bs4 import BeautifulSoup
import urllib.request
import ssl
import requests
import csv
import json
from datetime import datetime
context = ssl._create_unverified_context()
import pandas as pd
import requests


def get_new_feed():
    url = 'https://ncov.moh.gov.vn/web/guest/trang-chu'
    # page = urllib.request.urlopen(url, context=context)
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    new_feed = soup.find(class_='journal-content-article')
    print(new_feed)
    return new_feed

def to_soup(html):
    return BeautifulSoup(html, 'html.parser')

def get_journey():
    url = 'https://ncov.moh.gov.vn/dong-thoi-gian'
    page = requests.get(url, verify=False)
    soup = to_soup(page.text)
    journey = soup.find_all("div",class_='timeline')[:5]

    print(len(journey))

    dt_arr= []
    cnt_arr = []

    for j in journey:
        print(j.find("h3").text)
        dt_arr.append(j.find("h3").text)
        print(j.find("p").text)
        cnt_arr.append(j.find("p").text)


    return dt_arr,cnt_arr



def get_news2():
    url = 'https://ncov.moh.gov.vn/en/web/guest/trang-chu'
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    new_feeds = soup.find("div",class_ ="table-left").find_all("span", class_ ="font24")
    print('Viet nam')
    print('So ca nhiem:'+new_feeds[0].text)
    print('Dang dieu tri:'+new_feeds[1].text)
    print('Khoi:'+new_feeds[2].text)
    print('tu vong:'+new_feeds[3].text)
    print('The gioi')
    print('So ca nhiem:'+new_feeds[4].text)
    print('Dang dieu tri:'+new_feeds[5].text)
    print('Khoi:'+new_feeds[6].text)
    print('tu vong:'+new_feeds[7].text)



def get_city():
    url = 'https://covid19.gov.vn/'
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    new_feeds = soup.find("div",class_ ="home__statistical-list")
    print(new_feeds)

get_city()
