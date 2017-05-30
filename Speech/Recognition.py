import os
import OAuth
import urllib2
import json
import base64

def recognize(filePath, format, rate):
    #necessary parmeters:
    #format: pcm,wav, opus, speex, amr
    #rate: 8000, 16000
    #channel: 1
    #cuid: MAC
    #token: accessToken
    #len
    #speech:encode with base64
    url = 'http://vop.baidu.com/server_api'
    audioFile = open(filePath, 'rb')
    audio = audioFile.read()
    audioLen = int(os.path.getsize(filePath))
    speech = base64.b64encode(audio) 
    #get accessToken
    token = OAuth.getAccessToken()
    #init paras
    para = {
        "format":format,
        "rate":rate,
        "channel":1,
        "token":token,
        "cuid":"34-E6-AD-A1-23-E5",
        "len":audioLen,
        "speech":speech,
    }
    #send data
    post_data = json.dumps(para)
    headers = {
        'Content-type': 'application/json', 
        'Content-length': len(post_data)
        }
    request = urllib2.Request(url,post_data,headers=headers)
    response = urllib2.urlopen(request)
    resJson = response.read()
    resDict = json.loads(resJson)
    #get data
    errorCode = resDict['err_no']
    errorMsg = resDict['err_msg']
    if errorCode:
        print errorMsg
        print errorCode
        print len(resDict['sn'])
        return -1
    else:
        result = resDict['result']# it is a list of unicode objects
        return map(lambda x: x.encode('gbk'), result)# encode it with gb2132

