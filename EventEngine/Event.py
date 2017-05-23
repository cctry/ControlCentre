import time

class Event(object):
    
    def __init__(self):
        self.__id = hash(str(time.time()))
        self.__timestamp = time.time()
        self.__validity = True

    def getId(self):
        return self.__id
    
    def getTimestamp(self):
        return self.__timestamp
    
    def isValid(self):
        return self.__validity
    
    def setValidity(self, bool):
        self.__validity = bool


class OperationEvent(Event):

    def __init__(self, args):
        Event.__init__(self)
        self.object = args[0]
        self.intention = args[1]

class InquiryEvent(Event):

    def __init__(self,args):
        Event.__init__(self)