import Event
from threading import Thread
from Event import *
from libs import *
class EventProcessor(object):

    __objects = {'light':lightFunc, 'robot': None, 'AC': None}

    def __init__(self, queue, responseFactory):
        self.__eventQueue = queue
        self.__active = False# The trigger of the processor
        self.__thread = Thread(target=self.__Run)# Thread of the processor
        self.__scheduler = ScheduleManager()# Timing tasks manager

    def Start(self, callback):
        self.__callback = callback
        # Start the processor
        self.__active = True
        # Start the thread
        self.__thread.start()
        
    def __Run(self):
        # Run the processor
        while self.__active:
            # Fetch event from the queue
            event = self.__eventQueue.get()# Block if the queue is empty           
            handler = self.classify(event)# get the operation handler
            self.__callback(handler)           

    def classify(self, event):
        obj = event.getMsg('object')
        func = self.__objects[obj]
        return func(event)

    def lightFunc(self, event):
        place = event.getMsg('place')
        intent = event.getMsg('intent')
        time = event.getMsg('extra').get('time')
        handler = Light.getOperate(intent, place)
        if time is None:# Not a timing task
            return handler
        else:# schedule the timeing task
            pass
        
            
