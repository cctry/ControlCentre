from Queue import Queue
from EventFactory import *
from ResponseFactory import *
from EventProcessor import *
from ResponseProcessor import *

class EventEngine(object):    

    def __init__(self):
        self.__eventQueue = Queue()
        self.__responseQueue = Queue()
        self.__eventFactory = EventFactory(self.__eventQueue)
        self.__responseFactory = ResponseFactory(self.__responseQueue)
        self.__responseProcessor = ResponseProcessor(self.__responseQueue)
        self.__eventProcessor = EventProcessor(self.__eventQueue)
        self.__responseProcessor.Start(self.__eventCallback)
        self.__eventProcessor.Start()

    def __eventCallback(self, handler):
        self.__self.__responseFactory.getResponse(handler)# put response into response queue
    
    def setData(self, data):
        self.__eventFactory.prepareEvent()
        self.__eventFactory.addMsg(key = 'object', value = data['object'])
        self.__eventFactory.addMsg(key = 'intent', value = data['intent'])
        if data['extra'] != None:
            self.__eventFactory.addMsg(Dict = data['extra'])
        self.__eventFactory.getEvent()# put event into event queue      
        

        
            


    
    
