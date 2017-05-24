import Response
class ResponseFactory(object):
    def prepareResponse():
        response = Response()
        self.__response = response
    
    def addMsg(key = None, value = None, dict = None, dictBool = False):
        if !dictBool:
            self.__response.addMsg(key, value)
        else:
            for k, v in dict.items(): 
                self.__response.addMsg(k, v)
    
    def getResponse(handler):
        self.__response.setHandler(handler)