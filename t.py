import xlrd
from sql_modle import Sql_Modle

book = xlrd.open_workbook('information.xls')

sheet1 = book.sheets()[0]

nrows = sheet1.nrows

ss = Sql_Modle()


s = '''
【昵称】：{}
【性别】：{}
【城市】：{}
【工作】：{}
【微信】：{}
【自我介绍】：{}
【出生日期】：{}

'''

for x in range(1,nrows):
	r = sheet1.row_values(x)
	gender = r[1]
	birthday = r[2]
	city_name = r[3]
	work = r[4]
	my_self = r[5]
	nick_name = ''
	open_id = ''
	wechat = r[6]
	s_c = s.format(nick_name,gender,city_name,work,wechat,my_self,birthday)
	try:
		ss.insert(s_c,open_id,gender,city_name,wechat,my_self,work,birthday,nick_name)
	except Exception as e:
		print(e)
		continue
	

