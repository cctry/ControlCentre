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
        self.__responseProcessor.Start()
        self.__eventProcessor.Start(self.__eventCallback)

    def __eventCallback(self, handler):
        self.__responseFactory.getResponse(handler)# put response into response queue
    
    def setData(self, data):
        self.__eventFactory.prepareEvent()
        self.__eventFactory.addMsg(key = 'domain', value = data['domain'])
        self.__eventFactory.addMsg(key = 'object', value = data['object'])
        self.__eventFactory.addMsg(Dict = data['content'])
        self.__eventFactory.getEvent()# put event into event queue      
        

        
            


    
    
