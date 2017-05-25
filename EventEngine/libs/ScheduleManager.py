from apscheduler.schedulers.background import BackgroundScheduler
import time
class ScheduleManager(object):#TODO: cancel job

    def __init__(self):
        self.__event = {}
        self.__scheduler = BackgroundScheduler()
        self.__scheduler.start()
               
    def register(self, time, handler):
        self.__scheduler.add_job(handler, 'interval', secconds=time)

    def prepareJob(self, type, time):
        #'interval', 'date', 'cron'
        pass