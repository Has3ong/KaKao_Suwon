# -- coding: utf-8 --
import requests
from bs4 import BeautifulSoup
import re


class oWeather:
    session = requests.Session()
    addr = "http://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT"
    map_cityNum = {
        '화성': "001033"
    }

    def __init__(self, area="화성"):
        self.area = area
        self.addr = None
        self.result = None

        cityNum = oWeather.map_cityNum[area]
        if not cityNum:
            return
        self.addr = oWeather.addr + cityNum

    def Update(self):
        oWeather.session.encoding = 'utf-8'

        req = oWeather.session.get(self.addr)
        soup = BeautifulSoup(req.text, "html.parser")
        table = soup.find(class_="tbl_weather tbl_today3")

        t_ary = list(table.stripped_strings)

        # t_ary[2] = 오늘 t_ary[3] = 날짜
        # t_ary[7] 오전기온 t_ary[9] 상태 t_ary[11] = 강수확률
        # t_ary[13] 오후기온 t__ary[15] = 상태 t_ary[17] = 강수확률

        # t_ary[4] = 내일 t_ary[5] = 날짜
        # t_ary[19] 오전기온 t_ary[21] 상태 t_ary[23] = 강수확률
        # t_ary[25] 오후기온 t__ary[27] = 상태 t_ary[29] = 강수확률

        self.today = (
                "오늘의 날씨 🌤"
                + "\n🌥오전 기온 : " + t_ary[7] + ",  " + t_ary[9] + "\n☔강수확률 : " + t_ary[11]
                + "\n🌤오후 기온 : " + t_ary[13] + ",  " + t_ary[15] + "\n☔강수확률 : " + t_ary[17]
        )

        self.tomorrow = (
                "내일의 날씨 🌤"
                + "\n🌥오전 기온 : " + t_ary[19] + ",  " + t_ary[21] + "\n☔강수확률 : " + t_ary[23]
                + "\n🌤오후 기온 : " + t_ary[25] + ",  " + t_ary[27] + "\n☔강수확률 : " + t_ary[29]
                + "\n\n날씨 : 화성시 측정"
        )
