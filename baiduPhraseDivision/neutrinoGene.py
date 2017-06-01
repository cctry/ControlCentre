#!/usr/bin/python
# -.*?- coding: UTF-8 -.*?-

import cPickle as ObjectOp
import os

MainPo = os.path.split(os.path.realpath(__file__))[0]+'/'
def save(position, Ob):
	f = file(position,'w')
	ObjectOp.dump(Ob,f)
	f.close()

noun = {
	"query" : ["天气", "时间", "活动"],
	"app" : ["空调", "扫地机器人", "显示器", "插座", "日程表", "通知"]
}
save(MainPo+'noun.ob', noun)

action = {
	   "空调" :{
	   		"switchOn" :["打开", "启动", "开启"],
	   		"switchOff" :["关闭", "停止", "关上", "关掉"],
	   		"setPara" :["设置为.*?度", "调到.*?度"]
	   },
	   "扫地机器人" :{
	   		"switchOn" :["打开", "启动", "开启"],
	   		"switchOff" :["关闭", "停止", "关上", "关掉"],
	   		"setPara" :["打扫教室",]
	   },
	   "显示器" :{
	   		"switchOn" :["打开", "启动", "开启"],
	   		"switchOff" :["关闭", "停止", "关上", "关掉"],
	   		"setPara" :["显示.*?",]
	   },
	   "插座" :{
	   		"switchOn" :["打开", "启动", "开启"],
	   		"switchOff" :["关闭", "停止", "关上", "关掉"],
	   		"setPara" :["断电",]
	   },
	   "日程表" :{
	   	   	"switchOn" :["打开", "启动", "开启"],
	   		"switchOff" :["关闭", "停止", "关上", "关掉"],
	   		"setPara" :["提醒我.*?",]
	   },
	   "通知" :{
	   		"switchOn" :["打开", "启动", "开启"],
	   		"switchOff" :["关闭", "停止", "关上", "关掉"],
	   		"setPara" :["给小王发短信.*?", "通知小王.*?"]
	   },
	   "查询" :{
	   		"天气" :["天气怎么样", "天气如何", "下雨吗"], 
	   		"时间" :["几点了", "现在什么时间"],
	   		"活动" :["有什么安排", "哪些事", "有哪些任务", "要做什么"]
	   }
}
save(MainPo+'action.ob', action)

timeExp = {
	"具体时间" :["在.*?点", ".*?点钟"],
	"相对时间" :[".*?分钟后", "再过.*?分钟"],
	"时间段" :[".*?点到.*?点", ]	
}
save(MainPo+'time.ob', timeExp)
