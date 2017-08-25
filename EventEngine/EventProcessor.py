import Event
from threading import Thread
from Event import *
from utils import *
class EventProcessor(object):

    def __init__(self, queue):
        self.__eventQueue = queue
        self.__active = False# The trigger of the processor
        self.__thread = Thread(target=self.__Run)# Thread of the processor
        self.__scheduler = ScheduleManager.ScheduleManager()# Timing tasks manager

    def Start(self, callback):
        self.__callback = callback
        # Start the processor
        self.__active = True
        # Start the thread
        self.__thread.setDaemon(True)
        self.__thread.start()
        
    def __Run(self):
        # Run the processor
        while self.__active:
            # Fetch event from the queue
            event = self.__eventQueue.get()# Block if the queue is empty           
            handler = self.classify(event)# get the operation handler
            self.__callback(handler)           

    def lightFunc(self, event):
        place = event.getMsg('place')
        operation = event.getMsg('operation')
        handler = Light.getOperate(operation, place)
        return handler

    def weatherFunc(self, event):
        position = event.getMsg('position')

    def registerFunc(self, event):
        #need to get the information of wifi TODO
        #SmartConfig.register(getSSID(), getKey())
        pass

    __appObj = {'light': lightFunc, 'robot': None, 'AC': None, 'monitor': None}
    __queryObj = {'weather': weatherFunc, 'time': None, 'activity': None, 'register': registerFunc}
        
    def classify(self, event):
        domain = event.getMsg('domain')
        obj = event.getMsg('object')
        if domain == "app":
            func = self.__appObj[obj]
        if domain == "query":
            func = self.__queryObj[obj]
        return func(self, event)
