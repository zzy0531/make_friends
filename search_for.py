#encoding:utf-8
from sql_modle import Sql_Modle


class Search_User():

	def __init__(self):
		pass

	def look_for_user(self,content):
		try:
			content = content.replace('##','').strip()
			city_name = content.split('#')[0]
			gender = content.split('#')[1]
			return Sql_Modle().search_for_user(city_name,gender)
		except Exception as e:
			return '格式错啦，搜索符合要求的用户的格式为：##城市#性别，比如搜索北京的女生，那么回复：##北京#女。\n\n回复「格式」查看更多格式'