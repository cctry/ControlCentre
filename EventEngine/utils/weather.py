#coding=utf-8
import requests
#from Speech import Synthesis
from Speech import speak

KEY = 'yjdlftgpezhu7hqj'

def getDailyWeather(time):
    """
    time means the time of the required weather information (today: 0, tomorrow: 1, the day after tomorrow:2)
    :type time: str
    rtype: str
    """
    url = 'https://api.seniverse.com/v3/weather/daily.json'
    para = {
        'key':KEY,
        'location':'ip',
        'start': time,
        'days': '1',
    }
    r = requests.get(url, params=para)
    data = r.json()
    data = data['results']#list
    data = data[0]
    data = data['daily']
    day = ['今天', '明天', '后天']
    template = "'%s'白天'%s'，夜晚'%s'，最高气温'%s', 最低气温'%s'"

    return template%(day[time], data['text_day'], data['text_night'], data['high'], data['low'])

def getNow():
    """
    return the weather information of now
    rtype: str
    """
    url = 'https://api.seniverse.com/v3/weather/now.json'
    para = {
        'key':KEY,
        'location':'ip',
    }
    r = requests.get(url, params=para)
    data = r.json()
    data = data['results']#list
    data = data[0]
    now = data['now']
    for key in now.keys():
        now[key] = now[key].encode('utf8')
    tempertrue = str(data['temperature'])
    text = data['text']
    template = "现在'%s'，气温为'%s'摄氏度"
    return template%(text, tempertrue)

def getOperate(time):
    if time == 'now':
        data = getNow()
    else:
        data = getDailyWeather(time)
    def func():
        speak(data)

    return func
