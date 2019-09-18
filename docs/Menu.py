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

        self.Jong_Mon = []
        self.Jong_Tue = []
        self.Jong_Wen = []
        self.Jong_Thu = []
        self.Jong_Fri = []

    def Update(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        request = requests.get('https://www.suwon.ac.kr/index.html?menuno=1792')
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

        request = requests.get('https://www.suwon.ac.kr/index.html?menuno=1793')
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

        header = request.headers
        status = request.status_code
        is_HTTP_OK = request.ok

        self.Amarense = data

        self.SettingMenu()

    def SettingMenu(self):
        print(self.Amarense)
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

        self.Ama_Mon = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Mon + " 입니다."
        self.Ama_Tue = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Tue + " 입니다."
        self.Ama_Wen = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Wen + " 입니다."
        self.Ama_Thu = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Thu + " 입니다."
        self.Ama_Fri = self.Ama_Title + "🍽" + "\n\n오늘의 메뉴는\n" + self.Ama_Fri + " 입니다."
        self.Amarense.clear()

        self.Amarense.append(self.Ama_Mon)
        self.Amarense.append(self.Ama_Tue)
        self.Amarense.append(self.Ama_Wen)
        self.Amarense.append(self.Ama_Thu)
        self.Amarense.append(self.Ama_Fri)

        today = 0
        count = 0
        print(self.JongHab)
        for i in self.JongHab:
            if i == "Mom'sCook" or i == "LittleKitchen" or i == "돈까스코너":
                self.Jong_Title = i
            elif i == "중식":
                pass
            elif i == "":
                self.Jong_Title = "교직원 식당"

            else:
                if i[0] == "Mom'sCook" or i[0] == "LittleKitchen" or i[0] == "돈까스코너":
                    self.Jong_Title = i[0]
                elif i[0] == "중식":
                    pass
                elif i[0] == "":
                    self.Jong_Title = "교직원 식당"
                else:
                    if today == 0:
                        temp = " / ".join(i)
                        self.Jong_Mon.append(self.Jong_Title + "🍽" + "\n\n오늘의 메뉴는\n" + temp + " 입니다.")
                    if today == 1:
                        temp = " / ".join(i)
                        self.Jong_Tue.append(self.Jong_Title + "🍽" + "\n\n오늘의 메뉴는\n" + temp + " 입니다.")
                    if today == 2:
                        temp = " / ".join(i)
                        self.Jong_Wen.append(self.Jong_Title + "🍽" + "\n\n오늘의 메뉴는\n" + temp + " 입니다.")
                    if today == 3:
                        temp = " / ".join(i)
                        self.Jong_Thu.append(self.Jong_Title + "🍽" + "\n\n오늘의 메뉴는\n" + temp + " 입니다.")
                    if today == 4:
                        temp = " / ".join(i)
                        self.Jong_Fri.append(self.Jong_Title + "🍽" + "\n\n오늘의 메뉴는\n" + temp + " 입니다.")
                    today = (today + 1) % 5
        self.JongHab.clear()
        self.JongHab.append(self.Jong_Mon)
        self.JongHab.append(self.Jong_Tue)
        self.JongHab.append(self.Jong_Wen)
        self.JongHab.append(self.Jong_Thu)
        self.JongHab.append(self.Jong_Fri)
