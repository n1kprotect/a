import os
from sys import platform

from requests import get, post
from json import loads, load, dumps
from bs4 import BeautifulSoup

try:
    class App():
        def __init__(self, user_agent=None):
            self.user_agent = user_agent
        def Start(self, acr_id=None, as_html=False, **kwargs):
            """

            Values Checker / by nikitaprotect / lolz.guru/nikitaprotect


            :param acr_id: your acrid code / acrcloud.com
            :param as_html: True or False
            :return: JSON: {
                'title': 'Track Name',
                'artist': 'Artists Names',
                'album': 'Album Name',
                'release_date: 'Date of Released'
            }
            """
            get_page = get(f'https://www.doreso.com/{acr_id}', headers={
                'User-Agent': self.user_agent
            })
            soup = BeautifulSoup(get_page.text, 'html.parser')
            title = str(soup.find('h1', class_='text-white text-5xl font-medium')).split('\n')[1]
            artist = str(soup.find('span', class_='grey-text text-3xl font-bold')).split('\n')[1]
            album = str(soup.find('p', class_='text-white font-bold')).split('\n')[1]
            release_date = soup.find('div', class_='w-full md:w-auto md:ml-4')
            release_date = str(release_date.find('p', class_='text-white font-bold')).split('\n')[1]
            if as_html == True:
                    return soup.prettify()
            else:
                js = str("{'title': '" + title + "', 'album': '" + album + "', 'artist': '" + artist + "', 'release_date': '" + release_date + "'}")
                js = dumps(js)
                js = loads(js)
                return js
except ModuleNotFoundError:
    if platform == "linux" or platform == "linux2":
        try:
            os.system('pip3 install requests bs4')
            print('Завмсимости установленны! Перезапусти свой скрипт')
        except:
            exit('Error')
    elif platform == "win32":
        try:
            os.system('pip install requests bs4')
            print('Завмсимости установленны! Перезапусти свой скрипт')
        except:
            exit('Error')


