#encoding:utf-8
#数据库操作木块

import sqlite3

class Sql_Modle():

	def __init__(self,db_name = 'test.db'):
		self.conn = sqlite3.connect(db_name)

	def create(self):
		c = self.conn.cursor()

		c.execute('''
				CREATE TABLE USER_INFO(
					info TEXT NOT NUll,
					open_id TEXT,
					gender TEXT NOT NULL,
					city_name TEXT NOT NULL,
					wechat TEXT NOT NULL,
					my_self TEXT,
					work TEXT,
					birthday TEXT,
					nick_name TEXT);
			''')

		self.conn.commit()

	def delete(self):
		c = self.conn.cursor()

		c.execute('''
				DROP TABLE USER_INFO;
			''')

		self.conn.commit()

	def insert(self,info,open_id,gender,city_name,wechat,my_self,work,birthday,nick_name):
		c = self.conn.cursor()
		sql_tmp = 'INSERT INTO USER_INFO(info,open_id,gender,city_name,wechat,my_self,work,birthday,nick_name) VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(info,open_id,gender,city_name,wechat,my_self,work,birthday,nick_name)
		c.execute(sql_tmp)
		self.conn.commit()

	def search_for_user(self,city_name,gender):
		c = self.conn.cursor()
		sql_tmp = '''
			SELECT
				*
			FROM
				USER_INFO
			WHERE
				gender = '{}' and city_name like '%{}%'
		'''
		r = c.execute(sql_tmp.format(gender,city_name))
		return list(r)

	def find_all(self):
		c = self.conn.cursor()
		sql_tmp = '''
			SELECT
				*
			FROM
				USER_INFO;
		'''
		r = c.execute(sql_tmp)
		return list(r)


s = Sql_Modle()
print(len(s.find_all()))

