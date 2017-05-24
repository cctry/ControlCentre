class EventFactory(object):#TODO
    TYPE_OPERATION = 1
    TYPE_INQUIRY = 2
    
    def __init__(self, queue):
        self.__queue = queue