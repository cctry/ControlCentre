#coding=utf-8
import requests
from Speech import Synthesis
from Speech import speak

KEY = 'yjdlftgpezhu7hqj'

def getWeather(time):
    """
    time means the time of the required weather information (now, x-days)
    :type time: str
    :rtype: str
    """

    if time == 'now':
        data = getNow()
        text = data['text']
        tempertrue = str(data['temperature'])
        template = "今天'%s' 气温为'%s'摄氏度"
        res = template%(text, tempertrue)

    data = Synthesis.synthesize(res)
    return data

def getNow():
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
    return now
    
def getOperate(time):
    data = getWeather(time)
    def func():
        speak(data)