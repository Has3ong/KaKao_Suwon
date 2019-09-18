# -- coding: utf-8 --
import requests
import os, json, re
from bs4 import BeautifulSoup


class oNotice:
    def __init__(self):
        self.res = []

    def Update(self):
        self.res = []
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        request = requests.get('https://www.suwon.ac.kr/index.html?menuno=674')
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        repo_titles = soup.find('ul', class_='board_basic_list')
        data = repo_titles.find_all('a')


        for i in data:
            string = str(i)
            nDelimiter = string.find('title')
            rDelimiter = string.find(">")

            string = string[nDelimiter + 7 : rDelimiter - 1]
            self.res.append(string)
