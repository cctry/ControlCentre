import urllib
import json

def getWeather(code):
    url = 'http://www.weather.com.cn/data/sk/'+code'.html'
    res = urllib.urlopen(url)
    data = json.loads(res.read()).get(u'weatherinfo')
    #temperature: data['temp']
    #wind direction: data['WD']
    #wind speed: data['WS']
    #is rain: data['rain'] (ji)
    #relative humidity data['SD']
