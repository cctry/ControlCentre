import Event
import threading
import threading
from Event import *
class EventProcessor(object):

    def __init__(self, queue):
        self.eventQueue = queue
        self.__active = False# The trigger of the processor
        self.__thread = Thread(target = self.__Run)# Thread of the processor

    def Start(self):
        # Start the processor
        self.__active = True
        # Start the thread
        self.__thread.start()
        
    def __Run(self):
        # Run the processor
        while self.__active == True:
            # Fetch event from the queue
            event = self.eventQueue.get()# Block if the queue is empty