#encoding:utf-8
from sql_modle import Sql_Modle
import jieba
from gensim import corpora,models,similarities

#处理配对模块

'''
**
【昵称】：xx
【性别】：xx
【城市】：xx
【工作】：xx
【微信】：xx
【自我介绍】：xx
【出生日期】：xx
'''


class Match():
	"""docstring for ClassName"""
	def __init__(self,content,source):
		self.content = content
		self.source = source
		self.sql_modle = Sql_Modle()

	def result(self):

		try:
			s = self.content.replace('**','').strip()
			s_l = s.split('\n')
			if len(s_l) == 7:
				nick_name = s_l[0].split('】：')[1]
				gender = s_l[1].split('】：')[1]
				city_name = s_l[2].split('】：')[1]
				work = s_l[3].split('】：')[1]
				wechat = s_l[4].split('】：')[1]
				my_self = s_l[5].split('】：')[1]
				birthday = s_l[6].split('】：')[1]
				self.sql_modle.insert(s,self.source,gender,city_name,wechat,my_self,work,birthday,nick_name)
				return self.look_similar()
			else:
				return '''格式错误，如果你想搜索查看跟自己最匹配的异性，请复制下方文字进行修改并且回复：
					**
					【昵称】：xx
					【性别】：xx
					【城市】：xx
					【工作】：xx
					【微信】：xx
					【自我介绍】：xx
					【出生日期】：xx'''
		except Exception as e:
			return '''格式错误，如果你想搜索查看跟自己最匹配的异性，请复制下方文字进行修改并且回复：
					**
					【昵称】：xx
					【性别】：xx
					【城市】：xx
					【工作】：xx
					【微信】：xx
					【自我介绍】：xx
					【出生日期】：xx'''
		


	def look_similar(self):
		all_user = self.sql_modle.find_all()
		all_doc_list = []
		for doc in all_user:
			doc_list = [word for word in jieba.cut(doc)]
			all_doc_list.append(doc_list)

		doc_test_list = [word for word in jieba.cut(self.content)]
		dictionary = corpora.Dictionary(all_doc_list)
		corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
		
		doc_test_vec = dictionary.doc2bow(doc_test_list)
		tfidf = models.TfidfModel(corpus)

		index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
		sim = index[tfidf[doc_test_vec]]
		l = sorted(enumerate(sim), key=lambda item: -item[1])
		tmp_str = '以下是个目前跟你最匹配的用户\n\n:相似度：{}\n\n资料：{}'.format(l[0][1],all_user[l[0][0]])
		return tmp_str