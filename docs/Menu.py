# -- coding: utf-8 --
import requests
import os, json, re
from bs4 import BeautifulSoup


class oMenu:
    list = []

    def __init__(self):
        self.JongHab = []
        self.Amarense = []
        self.Menu = []

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
            data.append(tmp[4:tlength - 5])

        # with open(os.path.join(BASE_DIR, 'result1793.json'), 'w+') as json_file:
        # json.dump(data, json_file, indent='\t')

        header = request.headers
        status = request.status_code
        is_HTTP_OK = request.ok

        self.Amarense = data

        self.SettingToday()
        self.SettingMenu()

    def SettingToday(self):
        self.monLittle = (
                self.JongHab[1] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[2] + " 입니다."
        )
        self.monMom = (
                self.JongHab[8] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[9] + " 입니다."
        )
        self.monLittle2 = (
                self.JongHab[15] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[16] + " 입니다."
        )
        self.monDon = (
                self.JongHab[22] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[23] + " 입니다."
        )
        self.monGyo = (
                "교직원 식당" + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[29] + ", "
                + self.JongHab[35] + ", "
                + self.JongHab[41] + ", " + self.JongHab[47] + ", "
                + self.JongHab[53] + ", " + self.JongHab[59] + ", "
                + self.JongHab[65] + ", " + self.JongHab[71] + " 입니다."
        )
        '''
        self.monALittle = (
            self.Amarense[1] + "🍽"
            + "\n\n오늘의 메뉴는\n" + self.Amarense[2] + " 입니다."
        )
        self.monAMom = (
            self.Amarense[15] + "🍽"
            + "\n\n오늘의 메뉴는\n" + self.Amarense[16] + " 입니다."
        )
        self.monADon = (
            self.Amarense[22] + "🍽"
            + "\n\n오늘의 메뉴는\n" + self.Amarense[23] + " 입니다."
        )
        '''
        ###########################Monday##############################
        self.tueLittle = (
                self.JongHab[1] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[3] + " 입니다."
        )
        self.tueMom = (
                self.JongHab[8] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[10] + " 입니다."
        )
        self.tueLittle2 = (
                self.JongHab[15] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[17] + " 입니다."
        )
        self.tueDon = (
                self.JongHab[22] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[24] + " 입니다."
        )
        self.tueGyo = (
                "교직원 식당" + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[30] + ", "
                + self.JongHab[36] + ", "
                + self.JongHab[42] + ", " + self.JongHab[48] + ", "
                + self.JongHab[54] + ", " + self.JongHab[60] + ", "
                + self.JongHab[66] + ", " + self.JongHab[72] + " 입니다."
        )
        '''
        self.tueALittle = (
                self.Amarense[1] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[3] + " 입니다."
        )
        self.tueAMom = (
                self.Amarense[15] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[17] + " 입니다."
        )
        self.tueADon = (
                self.Amarense[22] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[24] + " 입니다."
        )
        '''
        #############################Tuesday############################
        self.wedLittle = (
                self.JongHab[1] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[4] + " 입니다."
        )
        self.wedMom = (
                self.JongHab[8] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[11] + " 입니다."
        )
        self.wedLittle2 = (
                self.JongHab[15] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[18] + " 입니다."
        )
        self.wedDon = (
                self.JongHab[22] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[25] + " 입니다."
        )
        self.wedGyo = (
                "교직원 식당" + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[31] + ", "
                + self.JongHab[37] + ", "
                + self.JongHab[43] + ", " + self.JongHab[49] + ", "
                + self.JongHab[55] + ", " + self.JongHab[61] + ", "
                + self.JongHab[67] + ", " + self.JongHab[73] + " 입니다."
        )
        '''
        self.wedALittle = (
                self.Amarense[1] + "🍽"
                + "\n\n\n오늘의 메뉴는\n" + self.Amarense[4] + " 입니다."
        )
        self.wedAMom = (
                self.Amarense[15] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[18] + " 입니다."
        )
        self.wedADon = (
                self.Amarense[22] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[25] + " 입니다."
        )
        '''
        #############################Wednesday############################
        self.thuLittle = (
                self.JongHab[1] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[5] + " 입니다."
        )
        self.thuMom = (
                self.JongHab[8] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[12] + " 입니다."
        )
        self.thuLittle2 = (
                self.JongHab[15] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[19] + " 입니다."
        )
        self.thuDon = (
                self.JongHab[22] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[26] + " 입니다."
        )
        self.thuGyo = (
                "교직원 식당" + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[32] + ", "
                + self.JongHab[38] + ", "
                + self.JongHab[44] + ", " + self.JongHab[50] + ", "
                + self.JongHab[56] + ", " + self.JongHab[62] + ", "
                + self.JongHab[68] + ", " + self.JongHab[74] + " 입니다."
        )
        '''
        self.thuALittle = (
                self.Amarense[1] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[5] + " 입니다."
        )
        self.thuAMom = (
                self.Amarense[15] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[19] + " 입니다."
        )
        self.thuADon = (
                self.Amarense[22] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[26] + " 입니다."
        )
        '''
        #############################Thursday############################
        self.friLittle = (
                self.JongHab[1] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[6] + " 입니다."
        )
        self.friMom = (
                self.JongHab[8] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[13] + " 입니다."
        )
        self.friLittle2 = (
                self.JongHab[15] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[20] + " 입니다."
        )
        self.friDon = (
                self.JongHab[22] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.JongHab[27] + " 입니다."
        )
        self.friGyo = (
                "교직원 식당" + "🍽"
                + "\n오늘의 메뉴는\n" + self.JongHab[33] + ", "
                + self.JongHab[39] + ", "
                + self.JongHab[45] + ", " + self.JongHab[51] + ", "
                + self.JongHab[57] + ", " + self.JongHab[63] + ", "
                + self.JongHab[69] + ", " + self.JongHab[75] + " 입니다."
        )
        '''
        self.friALittle = (
                self.Amarense[1] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[6] + " 입니다."
        )
        self.friAMom = (
                self.Amarense[15] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[20] + " 입니다."
        )
        self.friADon = (
                self.Amarense[22] + "🍽"
                + "\n\n오늘의 메뉴는\n" + self.Amarense[27] + " 입니다."
        )
        '''
        ##############################Friday###########################

        self.JongHab = []
        self.Amarense = []

    def SettingMenu(self):
        self.Menu.append(self.monLittle)
        self.Menu.append(self.monMom)
        self.Menu.append(self.monLittle2)
        self.Menu.append(self.monDon)
        self.Menu.append(self.monGyo)
        '''
        self.Menu.append(self.monALittle)
        self.Menu.append(self.monAMom)
        self.Menu.append(self.monADon)
        '''
        # index 8
        self.Menu.append(self.tueLittle)
        self.Menu.append(self.tueMom)
        self.Menu.append(self.tueLittle2)
        self.Menu.append(self.tueDon)
        self.Menu.append(self.tueGyo)
        '''
        self.Menu.append(self.tueALittle)
        self.Menu.append(self.tueAMom)
        self.Menu.append(self.tueADon)
        '''
        # index 16
        self.Menu.append(self.wedLittle)
        self.Menu.append(self.wedMom)
        self.Menu.append(self.wedLittle2)
        self.Menu.append(self.wedDon)
        self.Menu.append(self.wedGyo)
        '''
        self.Menu.append(self.wedALittle)
        self.Menu.append(self.wedAMom)
        self.Menu.append(self.wedADon)
        '''
        # index 24
        self.Menu.append(self.thuLittle)
        self.Menu.append(self.thuMom)
        self.Menu.append(self.thuLittle2)
        self.Menu.append(self.thuDon)
        self.Menu.append(self.thuGyo)
        '''
        self.Menu.append(self.thuALittle)
        self.Menu.append(self.thuAMom)
        self.Menu.append(self.thuADon)
        '''
        # index 32
        self.Menu.append(self.friLittle)
        self.Menu.append(self.friMom)
        self.Menu.append(self.friLittle2)
        self.Menu.append(self.friDon)
        self.Menu.append(self.friGyo)
        '''
        self.Menu.append(self.friALittle)
        self.Menu.append(self.friAMom)
        self.Menu.append(self.friADon)
        '''

