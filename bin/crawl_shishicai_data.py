#coding=utf-8
#desc:定时获取时时彩信息
from bs4 import BeautifulSoup
import time
import urllib2

def main():
	datestr = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	urllink = "http://baidu.lecai.com/lottery/draw/list/200?d=%s" % datestr
	urlres = urllib2.urlopen(urllink)
	pagedata = urlres.read()
	soup = BeautifulSoup(pagedata)
	search_results = soup.find('table',{'id':'draw_list'})
	index_results = search_results.findAll('td',{'class':'td2'})
	reward_results = search_results.findAll('td',{'class':'td3'})
	results = {}
	for i in range(0,len(index_results)):
		index_result = index_results[i]
		reward_result = reward_results[i].findAll('span',{'class':'ball_1'})

		reward_obj_list = []
		for obj in reward_result:
			reward_obj_list.append(obj.text)

		index_str = index_result.text.strip() #期数
		reward_str = " ".join(reward_obj_list) #获奖号码

		print index_str,reward_str
	# print index_results

if __name__ == '__main__':
	main()