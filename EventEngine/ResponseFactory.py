from Response import Response
class ResponseFactory(object):

    def __init__(self, queue):
        self.__queue = queue    
    
    def getResponse(self, handler):
        response = Response()
        response.setHandler(handler)
        self.__queue.put(response)