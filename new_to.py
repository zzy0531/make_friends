#encoding:utf-8

#主入口

import werobot
from match_deal import Match
from search_for import Search_User

robot = werobot.WeRoBot(token='renjia')


#处理新用户订阅消息
@robot.subscribe
def subscribe(message):
	return '你好，欢迎关注「路人甲」'


#处理用户的消息
@robot.handler
def msg_deal(message):
	if message.content.starstwith('**') or '昵称' in message.content:
		return Match(message.content,message.source).result()
	elif message.content.starstwith('##'):
		return Search_User().look_for_user(message.content)
	elif message.content = '格式':
		return '''
			如果你想要查看跟你最最匹配的的人，请复制以下我文字修改填写自己的资料：

			**
			【昵称】：xx
			【性别】：xx
			【城市】：xx
			【工作】：xx
			【微信】：xx
			【自我介绍】：xx
			【出生日期】：xx


			如果你想按照条件搜索符合条件的用户，请复制以下格式进行修改：

			##南京#女
			##南京#男
			'''
	else:
		return 'Hello World!'


'''
如果你想要查看跟你最最匹配的的人，请复制以下我文字修改填写自己的资料：

**
【昵称】：xx
【性别】：xx
【城市】：xx
【工作】：xx
【微信】：xx
【自我介绍】：xx
【出生日期】：xx


如果你想按照条件搜索符合条件的用户，请负责以下格式进行修改：

##南京#女
##南京#男
'''


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()