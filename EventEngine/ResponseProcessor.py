import Response
import threading
class ResponseProcessor(object):

    def __init__(self, queue):
        self.responseQueue = queue
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
            # Fetch response from the queue
            self.responseQueue.get()# Block if the queue is empty
            

    