import os
import OAuth
import urllib2
import urllib
import base64

def synthesize(text): # text must be encoded by utf-8 e.x. ChineseStr.decode('gbk).encode('utf8)
    """
    :type: str
    :rtype: binary data
    """
    url = 'http://tsn.baidu.com/text2audio'
    #get accessToken
    token = OAuth.getAccessToken()
    #init paras
    para = {
        "tex":text,
        "lan":'zh',
        "tok":urllib.quote(token),
        "ctp":urllib.quote('1'),
        "cuid":urllib.quote("34-E6-AD-A1-23-E5"),
    }
    #send data
    post_data = urllib.urlencode(para)
    request = urllib2.Request(url,post_data)
    response = urllib2.urlopen(request)
    headers = response.info().dict
    if headers['content-type'] == 'application/json':# something wrong
        print response.read()
    elif headers['content-type'] == 'audio/mp3':
        return response.read()# binary data
    else:
        print '!!'