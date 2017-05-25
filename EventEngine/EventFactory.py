from Event import *
class EventFactory(object):#TODO
    
    def __init__(self, queue):
        self.__queue = queue

    def prepareEvent(self):
        self.__event = Event()
    
    def addMsg(self, key = None, value = None, dict = None):
        if dict is None:
            self.__event.addMsg(key, value)
        else:
            for k, v in dict.items(): 
                self.__event.addMsg(k, v)
    
    def getEvent(self):
        self.__queue.put(self.__event)

