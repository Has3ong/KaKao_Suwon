# -- coding: utf-8 --
import requests
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote


class oDust:
    session = requests.Session

    def __init__(self):
        self.pm10 = ""
        self.pm25 = ""

    def Update(self):
        API_Key = unquote(
            'L0d9qiJ%2ByLZWrWY9eXSqNe8e%2BR4XTh5e3qBhzsIj7jNJixsnMqg4pTyIg1FaG%2FFtmz%2Bzir0805EJg%2BciCTQxIQ%3D%3D')
        url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
        queryParams = '?' + urlencode(
            {
                quote_plus('sidoName'): '경기',
                quote_plus('pageNo'): '1', quote_plus('numOfRows'): '7', quote_plus('serviceKey'): API_Key,
                quote_plus('ver'): '1.3'
            }
        )

        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode('utf-8')

        length = response_body.find('<stationName>고색동</stationName>')
        response_body = response_body[length:]

        start = response_body.find('<pm10Value>')
        end = response_body.find('</pm10Value>')

        self.pm10 = response_body[start + 11: end]

        start = response_body.find('<pm25Value>')
        end = response_body.find('</pm25Value>')

        self.pm25 = response_body[start + 11: end]
        self.pm10_emo = ""
        self.pm25_emo = ""

        if self.pm10 == '-':
            self.pm10_emo = " ❌"
        else:
            if int(self.pm10) <= 30:
                self.pm10_emo = " 😀"
            elif int(self.pm10) > 30 and int(self.pm10) <= 50:
                self.pm10_emo = " 😷"
            elif int(self.pm10) > 50 and int(self.pm10) <= 100:
                self.pm10_emo = " 😡"
            else:
                self.pm10_emo = " 👿"

        if self.pm25 == '-':
            self.pm25_emo = " ❌"
        else:
            if int(self.pm25) <= 15:
                self.pm25_emo = " 😀"
            elif int(self.pm25) and int(self.pm25) <= 25:
                self.pm25_emo = " 😷"
            elif int(self.pm25) > 25 and int(self.pm25) <= 50:
                self.pm25_emo = " 😡"
            else:
                self.pm25_emo = " 👿"

        self.today = (
                "\n\n🌫미세먼지 농도 : " + self.pm10 + self.pm10_emo
                + "\n🌫초미세먼지 농도 : " + self.pm25 + self.pm25_emo
                + "\n\n날씨 : 화성시 측정, 미세먼지 : 고색동 측정"
        )
