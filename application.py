# -- coding: utf-8 --
import os
import json
from flask import Flask, request, jsonify
import requests
import time
import threading

from Menu import oMenu
from Dust import oDust
from Weather import oWeather

app = Flask(__name__)

o_Menu = oMenu()
o_Weather = oWeather()
o_Dust = oDust()

#1day = 86400, 1hour = 3600
def Threading1d():
    pass
    #o_Menu.Update()
    o_Weather.Update()
    #threading.Timer(86400, Threading1d).start()
    
def Threading1h():
    pass
    #o_Dust.Update()
    #threading.Timer(3600, Threading1h).start()
    

@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']
    
    haksik_menu = False

    if content == u"소개":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "안녕하세요. 수원대학교 정보미디어학과/미디어SW학과 VRLab실에서 개발한 SuwonBot 입니다. 아직 많이 부족하지만 많은 이용 부탁드려요.\n피드백, 건의사항이 있으시면 아래의 메일로 보내주세요.\n같이 수원대학교 알리미를 개발할 UI, 디자인 쪽 개발자를 찾습니다. 마찬가지로 아래 메일로 보내주세요.\n메일 : khsh5592@naver.com"
                        }
                    }
                ]
            }
        }
    elif content == u"학식":
        haksik_menu = True
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard":{
                            "title" : "학식",
                            "description" : "종합강의동, 아마랜스 홀중 선택해주세요.",
                            "thumbnail": {
                              "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/MenuIndex.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRk1lbnVJbmRleC5wbmc=&docker_id=dbagmjvzeyafyjerlac&secure_session_id=D6joQ5pXfvp4D5PBFEVpFW8QdGaMd7XR"
                            },
                            "buttons": [
                                {
                                    "action": "message",
                                    "label": "종합강의동",
                                    "messageText": "종합강의동"
                                },
                                {
                                    "action":  "message",
                                    "label": "아마랜스 홀",
                                    "messageText": "아마랜스 홀"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"명령어":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "사용가능한 명령어는 '소개', '명령어', '미세먼지', '학식', '날씨'입니다."
                        }
                    }
                ]
            }
        }
    elif content == u"미세먼지":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "미세먼지."
                        }
                    }
                ]
            }
        }
    elif content == u"날씨":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "오늘의 날씨",
                                    "description" : o_Weather.today
                                },
                                {
                                    "title" : "내일의 날씨",
                                    "description" : o_Weather.tomorrow
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else :
        
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "아직 공부하고있습니다. 다른 명령어를 알고싶으시면 '명령어'를 입력해주세요. "
                        }
                    }
                ]
            }
        }
        
    if haksik_menu :
        pass
        
    return jsonify(dataSend)

if __name__ == "__main__":
    Threading1d()
    Threading1h()
    app.run(host='0.0.0.0')