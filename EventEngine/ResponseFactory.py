from Response import *
class ResponseFactory(object):

    def __init__(self, queue):
        self.__queue = queue
    def prepareResponse(self):
        response = Response()
        self.__response = response    
    def addMsg(self, key = None, value = None, dic = None, dictBool = False):
        if dictBool:
            for k, v in dic.items(): 
                self.__response.addMsg(k, v)
        else:
            self.__response.addMsg(key, value)     
    def getResponse(self):
        self.__queue.put(self.__response)