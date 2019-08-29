# -- coding: utf-8 --
import requests
import os, json, re
from bs4 import BeautifulSoup

class oMenu:
    list = []

    def __init__(self):
        self.JongHab = []
        self.Amarense = []

        self.Ama_Mon = ""
        self.Ama_Tue = ""
        self.Ama_Wen = ""
        self.Ama_Thu = ""
        self.Ama_Fri = ""

    def Update(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        request = requests.get('http://www.suwon.ac.kr/?menuno=762')
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        repo_titles = soup.select('div.section > div.subcont_inner > div.contents_table2 > table > tbody > tr > td')

        temp = []
        data = []

        for test in repo_titles:
            test = str(test)
            test = test.split()
            length = len(test)
            for i in range(0, length):
                text = ''.join(test)
            temp.append(text.split())

        length = len(temp)
        for i in range(0, length):
            tmp = temp[i][0]
            tlength = len(tmp)
            if i >= 2:
                data.append(tmp[4:tlength - 5].split('<br/>'))
            else:
                data.append(tmp[4:tlength - 5])

        # with open(os.path.join(BASE_DIR, 'result762.json'), 'w+') as json_file:
        # json.dump(data, json_file, indent='\t')

        header = request.headers
        status = request.status_code
        is_HTTP_OK = request.ok

        self.JongHab = data

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        request = requests.get('http://www.suwon.ac.kr/?menuno=1793')
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        repo_titles = soup.select('div.subcont > div.section > div.subcont_inner > div > table > tbody > tr > td')
        temp = []
        data = []

        for test in repo_titles:
            test = str(test)
            test = test.split()
            length = len(test)
            for i in range(0, length):
                text = ''.join(test)
            temp.append(text.split())

        length = len(temp)
        for i in range(0, length):
            tmp = temp[i][0]
            tlength = len(tmp)
            if i >= 2:
                data.append(tmp[4:tlength - 5].split('<br/>'))
            else:
                data.append(tmp[4:tlength - 5])

        # with open(os.path.join(BASE_DIR, 'result1793.json'), 'w+') as json_file:
        # json.dump(data, json_file, indent='\t')

        header = request.headers
        status = request.status_code
        is_HTTP_OK = request.ok

        self.Amarense = data

        print(self.Amarense)
        print(self.JongHab)

        self.SettingMenu()
        self.SettingToday()

    def SettingMenu(self):
        today = 0
        for i in self.Amarense:
            if i == "Mom'sCook" or i == "LittleKitchen" or i == "돈까스코너":
                self.Ama_Title = i
            if type(i) == list:
                if today == 0:
                    self.Ama_Mon = " / ".join(i)
                if today == 1:
                    self.Ama_Tue = " / ".join(i)
                if today == 2:
                    self.Ama_Wen = " / ".join(i)
                if today == 3:
                    self.Ama_Thu = " / ".join(i)
                if today == 4:
                    self.Ama_Fri = " / ".join(i)
                today = (today + 1) % 7

    def SettingToday(self):
        self.Ama_Mon = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Mon + " 입니다."
        self.Ama_Tue = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Tue + " 입니다."
        self.Ama_Wen = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Wen + " 입니다."
        self.Ama_Thu = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Thu + " 입니다."
        self.Ama_Fri = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Fri + " 입니다."

        self.Amarense.append(self.Ama_Mon)
        self.Amarense.append(self.Ama_Tue)
        self.Amarense.append(self.Ama_Wen)
        self.Amarense.append(self.Ama_Thu)
        self.Amarense.append(self.Ama_Fri)