import Queue
import Event, Response
import EventFactory, ResponseFactory
import ResponseProcessor, EventProcessor

class EventEngine(object):    

    def __init__(self):
        self.eventQueue = Queue.Queue()
        self.responseQueue = Queue.Queue()
        self.eventFactory = EventFactory.EventFactory(eventQueue)
        self.responseFactory = ResponseFactory.ResponseFactory(responseQueue)
        self.responseProcessor = ResponseProcessor.ResponseProcessor(responseQueue)
        self.eventProcessor = EventProcessor.EventProcessor(eventQueue)

        
            


    
    
