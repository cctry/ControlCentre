def getOperate(intent, place):
    if intent == 'on':
        def func():
            on(place)
    else:
        def func():
            off(place)
    return func

def getPlace(place):
    places = {'livingroom':0,'bedroom':1}# for demo
    return places.get(place)

def on(place):
    f = open('test.txt','w+')
    f.close()

def off(place):
    pass