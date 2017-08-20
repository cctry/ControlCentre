#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import cPickle as ObjectOp
#import os
#import time

#PresentPath = os.path.split(os.path.realpath(__file__))[0]+'/'
#noun = ObjectOp.load(PresentPath + 'noun.ob')
#action = ObjectOp.load(PresentPath + 'action.ob')

field = {
	"query" : ["天气" ],
	"app" : ["空调", "打扫", "显示器"]
}

objects = {
	   "空调" :{
	   		"switchOn" :["打开", "启动", "开启"],
	   		"switchOff" :["关闭", "停止", "关上", "关掉"],
	   },
	   "打扫" :{
	   		"switchOn" :["打开", "启动", "开启", "开始"],
	   		"switchOff" :["关闭", "停止", "关上", "关掉"],
	   },
	   "显示器" :{
	   		"switchOn" :["打开", "启动", "开启"],
	   		"switchOff" :["关闭", "停止", "关上", "关掉"],
	   },
	   "天气" :{
	   		"today" :["今天", "现在"], 
	   		"tomorrow" :["明天", "未来"],
	   }
}

def contain(str1, str2):
	if str1.find(str2) != -1:
		return 1
	else:
		return 0

#candidate = []
#for i in range(5):
#	candidate.append(raw_input())

candidate = getCandidate()

Flag = False
for i in candidate:
	for j,jv in field.items():
		for k in jv:
			if contain(i, k):
				Field = j
				Objects = k
				for l,lv in objects[Objects].items():
					for m in lv:
						if contain(i, m):
							Value = l
							Flag = True
if Flag:
	res = {
		"field" : Field,
		"objects" : Objects,
		"value" : Value
	}
else:
	res = {
		"field" : "error",
		"objects" : "command",
		"value" : "irregular"
	}

