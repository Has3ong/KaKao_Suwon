# -- coding: utf-8 --
import os
import json
from flask import Flask, request, jsonify
from datetime import datetime
import requests
import time
import threading

from docs.Menu import oMenu
from docs.Dust import oDust
from docs.Weather import oWeather
from docs.PhoneBook import oPhoneBook
from docs.BusShuttle import oBusShuttle
from docs.Calendar import oCalendar


app = Flask(__name__)

o_Menu = oMenu()
o_Weather = oWeather()
o_Dust = oDust()
o_PhoneBook = oPhoneBook()
o_BusShuttle = oBusShuttle()
o_Calendar = oCalendar()

#1day = 86400, 1hour = 3600
def Threading1d():
    o_Weather.Update()
    today = datetime.today().weekday()
    if today > 4:
        return 0
    o_Menu.Update()
    
    #threading.Timer(28800, Threading1d).start()
    
def Threading1h():
    o_Dust.Update()
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

    if content == u"시작하기":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard":{
                            "title" : "SuwonBot",
                            "description" : "안녕하세요. \n수원대학교 알림이 입니다. \n수원대학교에 관련된 정보를 간단하게 알려드릴게요!",
                            "thumbnail": {
                                "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Index.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9JbmRleC5wbmc=&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                            }
                        }
                    }
                ],
                "quickReplies": [
                    {
                        "label": "학교정보",
                        "action": "message",
                        "messageText": "학교정보 알려줘"
                    },
                    {
                        "label": "버스셔틀",
                        "action": "message",
                        "messageText": "셔틀버스"
                    },
                    {
                        "label": "학식",
                        "action": "message",
                        "messageText": "학식"
                    },
                    {
                        "label": "날씨",
                        "action": "message",
                        "messageText": "날씨"
                    },
                    {
                        "label": "종강 D-DAY",
                        "action": "message",
                        "messageText": "종강일 계산해줘"
                    }
                ]
            }
        }
    elif content == u"학교정보 알려줘" :
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard":{
                            "title" : "SuwonBot",
                            "description" : "안녕하세요. 수원대학교 정보미디어학과/미디어SW학과 VRLab실에서 개발한 SuwonBot 입니다. 아직 많이 부족하지만 많은 이용 부탁드려요. '\n명령어를 입력하시면 사용가능한 명령어가 나옵니다. \n피드백, 건의사항이 있으시면 아래의 메일로 보내주세요.\n\n메일 : suwonchatbot@gmail.com",
                            "thumbnail": {
                                "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Information.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9JbmZvcm1hdGlvbi5wbmc=&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                            }
                        }
                    }
                ],
                "quickReplies" : [
                    {
                        "label": "교내전화번호",
                        "action": "message",
                        "messageText": "교내전화번호"
                    },
                    {
                        "label": "학사일정",
                        "action": "message",
                        "messageText": "학사일정"
                    },
                    {
                        "label": "메인으로 돌아가기",
                        "action": "message",
                        "messageText": "시작하기"
                    },
                    {
                        "label": "개발중",
                        "action": "message",
                        "messageText": "개발중"
                    }
                ]
            }
        }
        
    elif content == u"학식":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard":{
                            "title" : "학식",
                            "description" : "종합강의동, 아마랜스 홀중 선택해주세요. \n\n링크 : http://www.suwon.ac.kr/?menuno=762 \n링크 : http://www.suwon.ac.kr/?menuno=1793",
                            "thumbnail": {
                              "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                            },
                            "buttons": [
                                {
                                    "action": "message",
                                    "label": "종합강의동",
                                    "messageText": "종합강의동 학식 알려주세요"
                                },
                                {
                                    "action":  "message",
                                    "label": "아마랜스 홀",
                                    "messageText": "아마랜스홀 학식 알려주세요"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"종합강의동 학식 알려주세요":
        today = datetime.today().weekday()
        if today > 4:
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs":[
                        {
                            "carousel":{
                                "type": "basicCard",
                                "items":[
                                    {
                                        "title" : "종합강의동 학식",
                                        "description" : "오늘은 휴일입니다.",
                                        "thumbnail" :{
                                            "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(dataSend)
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs":[
                {
                    "carousel":{
                        "type": "basicCard",
                        "items":[
                            {
                                "title" : "LittleKitchen",
                                "description" : o_Menu.Menu[today * 8],
                                "thumbnail" : {
                                    "imageUrl" : {
                                        "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
                                }
                            },
                            {
                                "title" : "Mom's Cook",
                                "description" : o_Menu.Menu[today * 8+1],
                                "thumbnail" : {
                                    "imageUrl" : {
                                        "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
                                }
                            },
                            {
                                "title" : "LittleKitchen",
                                "description" : o_Menu.Menu[today * 8+2],
                                "thumbnail" : {
                                    "imageUrl" : {
                                        "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
                                }
                            },
                            {
                                "title" : "돈까스 코너",
                                "description" : o_Menu.Menu[today * 8+3],
                                "thumbnail": {
                                    "imageUrl" : {
                                        "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
                                }
                            },
                            {
                                "title" : "교직원 식당",
                                "description" : o_Menu.Menu[today * 8+4],
                                "thumbnail": {
                                    "imageUrl" : {
                                        "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
                                }
                            }
                        ]
                    }
                }
                ]
            }
        }
    elif content == u"아마랜스홀 학식 알려주세요":
        today = datetime.today().weekday()
        print(today, datetime.today())
        if today > 4:
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs":[
                        {
                            "carousel":{
                                "type": "basicCard",
                                "items":[
                                    {
                                        "title" : "아마랜스홀 학식",
                                        "description" : "오늘은 휴일입니다.",
                                        "thumbnail":{
                                            "imageUrl": "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(dataSend)
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs":[
                    {
                        "carousel":{
                            "type": "basicCard",
                            "items":[
                                {
                                    "title" : "LittleKitchen",
                                    "description" : o_Menu.Menu[today * 8+5],
                                    "thumbnail" : {
                                        "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
                                },
                                {
                                    "title" : "Mom's Cook",
                                    "description" : o_Menu.Menu[today * 8+6],
                                    "thumbnail": {
                                        "imageUrl": "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
                                },
                                {
                                    "title" : "돈까스 코너",
                                    "description" : o_Menu.Menu[today * 8+7],
                                    "thumbnaiul": {
                                        "imageUrl": "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Menu.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9NZW51LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
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
                            "text" : "사용가능한 명령어는 '소개', '미세먼지', '학식', '날씨', '교내전화번호', '셔틀버스', '학사일정'입니다."
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
                                    "description" : "" ,
                                    "thumbnail": {
                                        "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Today.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9Ub2RheS5wbmc=&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    },
                                    "buttons": [
                                        {
                                            "action" : "message",
                                            "label" : "오늘의 날씨",
                                            "messageText" : "오늘 날씨 알려줘"
                                        }
                                    ]
                                },
                                {
                                    "title" : "내일의 날씨",
                                    "description" : "",
                                    "thumbnail" : {
                                        "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Tomorow.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9Ub21vcm93LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    },
                                    "buttons": [
                                        {
                                            "action" : "message",
                                            "label" : "내일의 날씨",
                                            "messageText" : "내일 날씨 알려줘"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
        '''
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
                                    "description" : o_Weather.today + o_Dust.today,
                                    "thumbnail" : {
                                        "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Today.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9Ub2RheS5wbmc=&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
                                },
                                {
                                    "title" : "내일의 날씨",
                                    "description" : o_Weather.tomorrow,
                                    "thumbnail" :{
                                        "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Tomorow.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9Ub21vcm93LnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
        '''
    elif content == u"오늘 날씨 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard":{
                            "title": "",
                            "description" : o_Weather.today + o_Dust.today
                        }
                    }
                ]
            }
        }
        
    elif content == u"내일 날씨 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard":{
                            "title": "",
                            "description" : o_Weather.tomorrow
                        }
                    }
                ]
            }
        }
    elif content == u"종강일 계산해줘" :
        nowtime = datetime.now()
        endtime = datetime(2019, 6, 24, 0, 0, 0)
        
        d_days = (endtime-nowtime).days
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs" : [
                    {
                        "basicCard" : {
                            "title" : "종강일 계산하기",
                            "description" : "종강까지 " + str(d_days) + " 일 남았습니다.",
                            "thumbnail": {
                              "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_DDAY.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9EREFZLnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                            }
                        }
                    }
                ]
            }
        }
    elif content == u"학사일정" :
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "학사일정",
                                    "description" : "링크 : http://www.suwon.ac.kr/?menuno=727",
                                    "buttons": [
                                    {
                                        "action" : "message",
                                        "label" : "1학기 학사일정",
                                        "messageText" : "1학기 학사일정 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "2학기 학사일정",
                                        "messageText" : "2학기 학사일정 알려줘"
                                    },
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"1학기 학사일정 알려줘" :
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "1월 학사일정",
                                    "description" : o_Calendar.Jan
                                },
                                {
                                    "title" : "2월 학사일정",
                                    "description" : o_Calendar.Feb
                                },
                                {
                                    "title" : "3월 학사일정",
                                    "description" : o_Calendar.Mar
                                },
                                {
                                    "title" : "4월 학사일정",
                                    "description" : o_Calendar.Apr
                                },
                                {
                                    "title" : "5월 학사일정",
                                    "description" : o_Calendar.May
                                },
                                {
                                    "title" : "6월 학사일정",
                                    "description" : o_Calendar.June
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"2학기 학사일정 알려줘" :
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "7월 학사일정",
                                    "description" : o_Calendar.July
                                },
                                {
                                    "title" : "8월 학사일정",
                                    "description" : o_Calendar.Aug
                                },
                                {
                                    "title" : "9월 학사일정",
                                    "description" : o_Calendar.Sep
                                },
                                {
                                    "title" : "10월 학사일정",
                                    "description" : o_Calendar.Oct
                                },
                                {
                                    "title" : "11월 학사일정",
                                    "description" : o_Calendar.Nov
                                },
                                {
                                    "title" : "12월 학사일정",
                                    "description" : o_Calendar.Dec
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"셔틀버스":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "셔틀버스",
                                    "description" : "",
                                    "thumbnail": {
                                        "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Bus1.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9CdXMxLnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    },
                                    "buttons": [
                                    {
                                        "action" : "message",
                                        "label" : "교내 셔틀 시간표",
                                        "messageText" : "교내 셔틀 시간표 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "상록수 셔틀버스",
                                        "messageText" : "상록수 셔틀버스 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "송내 셔틀버스",
                                        "messageText" : "송내 셔틀버스 알려줘"
                                    }
                                    ]
                                },
                                {
                                    "title" : "셔틀버스",
                                    "description" : "",
                                    "thumbnail" : {
                                        "imageUrl" : "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Bus2.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9CdXMyLnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    },
                                    "buttons": [
                                    {
                                        "action" : "message",
                                        "label" : "금정 셔틀버스",
                                        "messageText" : "금정 셔틀버스 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "성남(야탑) 셔틀버스",
                                        "messageText" : "성남 셔틀버스 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "수원 셔틀버스",
                                        "messageText" : "수원 셔틀버스 알려줘"
                                    }
                                ]
                                },
                                {
                                    "title" : "셔틀버스",
                                    "description" : "링크 : http://www.suwon.ac.kr/?menuno=655",
                                    "thumbnail":{
                                        "imageUrl": "https://proxy.goorm.io//service/5ccda9890e70de7aa094ede1_dbagmjvzeyafyjerlac.run.goorm.io/9080//file/load/App_Bus3.png?path=d29ya3NwYWNlJTJGU3V3b25Cb3QlMkZJbWFnZSUyRkFwcF9CdXMzLnBuZw==&docker_id=dbagmjvzeyafyjerlac&secure_session_id=ukvGkLMs6b_IfPgimh-pjWVtciFqdpSu"
                                    },
                                    "buttons": [
                                    {
                                        "action" : "message",
                                        "label" : "강남 셔틀버스",
                                        "messageText" : "강남 셔틀버스 알려줘"
                                    }
                                ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"교내 셔틀 시간표 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_BusShuttle.InShuttle
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
    elif content == u"송내 셔틀버스 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_BusShuttle.OutShuttle_SongNae
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
    elif content == u"상록수 셔틀버스 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_BusShuttle.OutShuttle_SangRokSu
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
    elif content == u"금정 셔틀버스 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_BusShuttle.OutShuttle_GeumJeong
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
    elif content == u"성남 셔틀버스 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_BusShuttle.OutShuttle_SeongNam
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
    elif content == u"수원 셔틀버스 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_BusShuttle.OutShuttle_Suwon
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
    elif content == u"강남 셔틀버스 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_BusShuttle.OutShuttle_GangNam
                                }
                            ]
                        }
                    }
                ]
            }
        }
    #신도림 셔틀버스 사라짐
    elif content == u"신도림 셔틀버스 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_BusShuttle.OutShuttle_SinDoRim
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
    elif content == u"교내전화번호":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "교내전화번호",
                                    "description" : "교내 안내 031-220-2114",
                                    "buttons": [
                                    {
                                        "action" : "message",
                                        "label" : "인문사회대학",
                                        "messageText" : "인문사회대학 전화번호 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "경상대학",
                                        "messageText" : "경상대학 전화번호 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "공과대학",
                                        "messageText" : "공과대학 전화번호 알려줘"
                                    }
                                    ]
                                },
                                {
                                    "title" : "교내전화번호",
                                    "description" : "교내 안내 031-220-2114",
                                    "buttons": [
                                    {
                                        "action" : "message",
                                        "label" : "ICT 융합대학",
                                        "messageText" : "ICT 융합대학 전화번호 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "미술대학",
                                        "messageText" : "미술대학 전화번호 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "음악대학",
                                        "messageText" : "음악대학 전화번호 알려줘"
                                    }
                                ]
                                },
                                {
                                    "title" : "교내전화번호",
                                    "description" : "교내 안내 031-220-2114",
                                    "buttons": [
                                    {
                                        "action" : "message",
                                        "label" : "융합문화 예술대학",
                                        "messageText" : "융합문화 예술대학 전화번호 알려줘"
                                    },
                                    {
                                        "action" : "message",
                                        "label" : "건강과학대학",
                                        "messageText" : "건강과학대학 전화번호 알려줘"
                                    }
                                ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"인문사회대학 전화번호 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_PhoneBook.InMun1
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"경상대학 전화번호 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_PhoneBook.GyungSang1
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"공과대학 전화번호 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_PhoneBook.GongGwa1
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"ICT 융합대학 전화번호 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_PhoneBook.ICT1
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"미술대학 전화번호 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_PhoneBook.Art1
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"음악대학 전화번호 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_PhoneBook.Music
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"융합문화 예술대학 전화번호 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_PhoneBook.MunHwa1
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"건강과학대학 전화번호 알려줘":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : o_PhoneBook.GunGang1
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
                            "text" : "아직 공부하고있습니다."
                        }
                    }
                ]
            }
        }
        
    return jsonify(dataSend)

if __name__ == "__main__":
    Threading1d()
    Threading1h()
    app.run(host='0.0.0.0')