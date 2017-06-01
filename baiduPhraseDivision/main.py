#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cPickle as ObjectOp
import os
import OUTSIDE
import stringzi
import time
import re


PresentPath = os.path.split(os.path.realpath(__file__))[0]+'/'
noun = ObjectOp.load(PresentPath + 'noun.ob')
timeExp = ObjectOp.load(PresentPath + 'time.ob')
action = ObjectOp.load(PresentPath + 'action.ob')

day = {
	"今天" :0,
	"明天" :1,
	"后天" :2
}
daystage = {
	"上午" :1,
	"下午" :2, 
	"晚上" :3 
}

while OUTSIDE.active :
	
	PTime = map(int, time.strftime("%X", time.localtime()).split(":"))[:2] #获取当前时间 哪一天、什么时间段、几点、几分
	PTime.insert(0,0)
	PTime.insert(0,0)
	timemode = 0 # 0模糊时间、1具体时间、2相对时间、3时间段

	words = raw.input()#words = OUTSIDE.grasp().strip()
	DOMAIN = OBJECT = OPERATION = PARAMETER = STARTTIME = ENDTIME = "DEFAULT"

#time finding and cut
	STime = PTime
	for k in day.keys():
		po = words.index(k)
		if po >= 0:
			STime[0] = day[k]
			words = words.split(k)[1]
			break
	for k in daystage.keys():
		po = words.index(k)
		if po >= 0:
			STime[2] = daystage[k]
			words = words.split(k)[1]
			break

	for k in timeExp["具体时间"]
		m = re.match(k, words)
		if m.group() :
			timemode = 1
			STime[2:] = [conv(m.group), 0]
			break
	




#domain deside

#object deside

#operation deside

#parameter deside




	res = {
		"domain" : DOMAIN
		"object" : OBJECT
		"content" : {
			"operation" : OPERATION
			"parameter" : PARAMETER
			"startTime" : STARTTIME
			"endTime" : ENDTIME 
		}
	}

#下为样例


res = {
	"domain" : "app"
	"object" : "显示器"
	"content" : {
		"operation" : "setPara"
		"parameter" : "显示器测试"
		"startTime" : "0:15:30"
		"endTime" : "0:16:30"
	}
}

res = {
	"domain" : "query"
	"object" : "天气"
	"content" : {
		"startTime" : "1:00:00"
	}
}

