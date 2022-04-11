import requests
from bs4 import BeautifulSoup
import lxml
from time import time


def get_posts():
    link = 'https://lenta.ru/parts/news/'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36'}
    res = requests.get(link, headers=header).text

    # with open('info.txt', 'r', encoding='utf-8') as file:
    #     res = file.read()

    soup = BeautifulSoup(res, 'lxml')
    list_items = soup.find_all(class_='parts-page__item')
    fill_list = []
    for item in list_items:
        href = item.find('a').get('href')
        if href[0] != '/':
            continue
        try:
            title = item.find('h3').text
        except:
            continue
        fill_list.append({'title': title, 'href': 'https://lenta.ru' + href})

    return fill_list


def get_send(text: str):
    link = 'https://discord.com/api/v9/channels/949692477248524388/messages'
    header = {
        'authorization': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36'}
    data = {'content': text, 'nonce': str(int(time())), 'tts': False}
    requests.post(link, headers=header, json=data).json()


def loop_news():
    pass


if __name__ == '__main__':
    loop_news()
    with open('config.txt', 'r', encoding='utf-8') as file:
        file.read()

# pip freeze requairaments
# git config --global user.name "Latyshevdp"
# $ git config --global user.email "latyshevdp@yandex.ru"