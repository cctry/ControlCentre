from Event import *
class EventFactory(object):#TODO
    TYPE_OPERATION = 1
    TYPE_INQUIRY = 2
    
    def __init__(self, queue):
        self.__queue = queue

    def prepareEvent(self, queue):
        event = Event()
        self.__event = event
    
    def addMsg(self, key = None, value = None, dict = None, dictBool = False):
        if !dictBool:
            self.__event.addMsg(key, value)
        else:
            for k, v in dict.items(): 
                self.__event.addMsg(k, v)
    
    def getEvent(self):
        self.__queue.put(self.__event)