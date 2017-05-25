from Queue import Queue
from EventFactory import *
from ResponseFactory import *
from EventProcessor import *
from ResponseProcessor import *

class EventEngine(object):    

    def __init__(self):
        self.--eventQueue = Queue()
        self.--responseQueue = Queue()
        self.--eventFactory = EventFactory(eventQueue)
        self.--responseFactory = ResponseFactory(responseQueue)
        self.--responseProcessor = ResponseProcessor(responseQueue)
        self.--eventProcessor = EventProcessor(eventQueue)
        self.--responseProcessor.Start()
        self.--eventProcessor.Start()

    
    def setData(data):
        self.__eventFactory.prepareEvent()
        self.__eventFactory.addMsg(key = 'object', value = data['object'])
        self.__eventFactory.addMsg(key = 'intent', value = data['intent'])
        if data['extra'] != None:
            self.__eventFactory.addMsg(dict = data['extra'])
        self.__eventFactory.getEvent()# put event into event queue      
        

        
            


    
    
