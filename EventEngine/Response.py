import time
class Response(object):
    
    def __init__(self):
        self.__id = hash(str(time.time()))
        self.__timestamp = time.time()
        
    def getId(self):
        return self.__id
    
    def getTimestamp(self):
        return self.__timestamp

    def setHandler(self, handler):
        self.__handler = handler

    def getHandler(self):
        return self.__handler