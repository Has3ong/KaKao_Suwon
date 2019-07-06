

미세먼지
class : oDust, object : o_Dust
self.pm10 -> 미세먼지 농도
self.pm25 -> 초 미세먼지 농도
OpenAPI로 구현

날씨
class : oWeather, object : o_Weather
OpenAPI로 구현 예정

메뉴
class : oMenu, object : o_Menu 
종합강의동
self.monLit -> 월요일 Little Kitchen
self.monDon -> 월요일 돈까스코너
self.monGyo -> 월요일 교직원식당
self.monMom -> 월요일 Mom'sCook
아마랜스홀
self.monALit -> 월요일 Little Kitchen
self.monAMon -> 월요일 돈까스코너
self.monAMom -> 월요일 Mom'sCook

셔틀버스
class : oBusShuttle, object : o_BusShuttle
self.InShuttle -> 교내셔틀
self.OutShuttle_** -> 교외 ** 셔틀  ** -> 지역이름

교내전화번호
class : oPhoneBOok, object : o_PhoneBook

공지사항
class : oNotice, object : i_Notice

알림이 공지사항
class : sNotice, object : s_Notice