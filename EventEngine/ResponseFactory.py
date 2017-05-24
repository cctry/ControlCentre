from Response import *
class ResponseFactory(object):

    def __init__(self, queue):
        self.__queue = queue

    def prepareResponse(self, queue):
        response = Response()
        self.__response = response
    
    def addMsg(self, key = None, value = None, dict = None, dictBool = False):
        if !dictBool:
            self.__response.addMsg(key, value)
        else:
            for k, v in dict.items(): 
                self.__response.addMsg(k, v)
    
    def getResponse(self):
        self.__queue.put(self.__response)