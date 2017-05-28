import time

class Event(object):
    def __init__(self):
        self.__id = hash(str(time.time()))
        self.__timestamp = time.time()
        self.__validity = True
        self.__msg = {}
    def getId(self):
        return self.__id
    def getTimestamp(self):
        return self.__timestamp
    def isValid(self):
        return self.__validity
    def setValidity(self, Bool):
        self.__validity = Bool
    def addMsg(self, key, value):
        self.__msg.update({key: value})
    def getMsg(self, key):
        temp = self.__msg.get(key)
        if temp == None:
            # exception
            return -1
        else:
            return temp
            