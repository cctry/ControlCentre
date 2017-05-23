import urllib
import urllib2
import json
#Keys for the application
AppID="9671682"
APIKey="VqYYrrs4Ke0k7CUm1t7l4bfn"
SecretKey="811f33aa36a1098ae84667edffb88a03"

def getAccessToken():
    url = "https://openapi.baidu.com/oauth/2.0/token"
    para = {
        'grant_type': 'client_credentials',
        'client_id': APIKey,
        'client_secret': SecretKey
    }
    post_data = urllib.urlencode(para)
    req = urllib2.Request(url,post_data)
    resp = urllib2.urlopen(req)
    resJson = resp.read()
    resDict = json.loads(resJson)
    accessToken = resDict["access_token"].encode('ASCII')
    return accessToken

