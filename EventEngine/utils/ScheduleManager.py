from apscheduler.schedulers.background import BackgroundScheduler
import time
class ScheduleManager(object):
    #TODO: cancel job
    def __init__(self):
        self.__event = {}
        self.__scheduler = BackgroundScheduler()
        self.__scheduler.start()
               
    def register(self, time, handler):
        self.__scheduler.add_job(handler, 'interval', seconds=time)

    def prepareJob(self, timeType, t):
        # t: 'interval', 'date', 'cron'
        pass
    