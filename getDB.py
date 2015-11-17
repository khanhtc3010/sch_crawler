# -*- coding: utf-8 -*-
import requests, codecs, mechanize
from pymongo import MongoClient
from bs4 import BeautifulSoup
#############################################
client = MongoClient('localhost', 27017) #connext to mongodb
db = client.japanesecenterDB	#create a database
japCenter = db.japCenter #create a collection
#############################################
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0')]
#############################################
prefectureDict = {
	"北海道":{"ja_name": "北海道", "prefecture_id": 1, "vi_name": "Hokkaido"},
	"青森県":{"ja_name": "青森県", "prefecture_id": 2, "vi_name": "Aomori"},
	"岩手県":{"ja_name": "岩手県", "prefecture_id": 3, "vi_name": "Iwate"},
	"宮城県":{"ja_name": "宮城県", "prefecture_id": 4, "vi_name": "Miyagi"},
	"秋田県":{"ja_name": "秋田県", "prefecture_id": 5, "vi_name": "Akita"},
	"山形県":{"ja_name": "山形県", "prefecture_id": 6, "vi_name": "Yamagata"},
	"福島県":{"ja_name": "福島県", "prefecture_id": 7, "vi_name": "Fukushima"},
	"茨城県":{"ja_name": "茨城県", "prefecture_id": 8, "vi_name": "Ibaraki"},
	"栃木県":{"ja_name": "栃木県", "prefecture_id": 9, "vi_name": "Tochigi"},
	"群馬県":{"ja_name": "群馬県", "prefecture_id": 10, "vi_name": "Gunma"},
	"埼玉県":{"ja_name": "埼玉県", "prefecture_id": 11, "vi_name": "Saitama"},
	"千葉県":{"ja_name": "千葉県", "prefecture_id": 12, "vi_name": "Chiba"},
	"東京都":{"ja_name": "東京都", "prefecture_id": 13, "vi_name": "Tokyo"},
	"神奈川県":{"ja_name": "神奈川県", "prefecture_id": 14, "vi_name": "Kanagawa"},
	"新潟県":{"ja_name": "新潟県", "prefecture_id": 15, "vi_name": "Niigata"},
	"富山県":{"ja_name": "富山県", "prefecture_id": 16, "vi_name": "Toyama"},
	"石川県":{"ja_name": "石川県", "prefecture_id": 17, "vi_name": "Ishikawa"},
	"福井県":{"ja_name": "福井県", "prefecture_id": 18, "vi_name": "Fukui"},
	"山梨県":{"ja_name": "山梨県", "prefecture_id": 19, "vi_name": "Yamanashi"},
	"長野県":{"ja_name": "長野県", "prefecture_id": 20, "vi_name": "Nagano"},
	"岐阜県":{"ja_name": "岐阜県", "prefecture_id": 21, "vi_name": "Gifu"},
	"静岡県":{"ja_name": "静岡県", "prefecture_id": 22, "vi_name": "Shizuoka"},
	"愛知県":{"ja_name": "愛知県", "prefecture_id": 23, "vi_name": "Aichi"},
	"三重県":{"ja_name": "三重県", "prefecture_id": 24, "vi_name": "Mie"},
	"滋賀県":{"ja_name": "滋賀県", "prefecture_id": 25, "vi_name": "Shiga"},
	"京都府":{"ja_name": "京都府", "prefecture_id": 26, "vi_name": "Kyoto"},
	"大阪府":{"ja_name": "大阪府", "prefecture_id": 27, "vi_name": "Osaka"},
	"兵庫県":{"ja_name": "兵庫県", "prefecture_id": 28, "vi_name": "Hyogo"},
	"奈良県":{"ja_name": "奈良県", "prefecture_id": 29, "vi_name": "Nara"},
	"和歌山県":{"ja_name": "和歌山県", "prefecture_id": 30, "vi_name": "Wakayama"},
	"鳥取県":{"ja_name": "鳥取県", "prefecture_id": 31, "vi_name": "Tottori"},
	"島根県":{"ja_name": "島根県", "prefecture_id": 32, "vi_name": "Shimane"},
	"岡山県":{"ja_name": "岡山県", "prefecture_id": 33, "vi_name": "Okayama"},
	"広島県":{"ja_name": "広島県", "prefecture_id": 34, "vi_name": "Hiroshima"},
	"山口県":{"ja_name": "山口県", "prefecture_id": 35, "vi_name": "Yamaguchi"},
	"徳島県":{"ja_name": "徳島県", "prefecture_id": 36, "vi_name": "Tokushima"},
	"香川県":{"ja_name": "香川県", "prefecture_id": 37, "vi_name": "Kagawa"},
	"愛媛県":{"ja_name": "愛媛県", "prefecture_id": 38, "vi_name": "Ehime"},
	"高知県":{"ja_name": "高知県", "prefecture_id": 39, "vi_name": "Kochi"},
	"福岡県":{"ja_name": "福岡県", "prefecture_id": 40, "vi_name": "Fukuoka"},
	"佐賀県":{"ja_name": "佐賀県", "prefecture_id": 41, "vi_name": "Saga"},
	"長崎県":{"ja_name": "長崎県", "prefecture_id": 42, "vi_name": "Nagasaki"},
	"熊本県":{"ja_name": "熊本県", "prefecture_id": 43, "vi_name": "Kumamoto"},
	"大分県":{"ja_name": "大分県", "prefecture_id": 44, "vi_name": "Oita"},
	"宮崎県":{"ja_name": "宮崎県", "prefecture_id": 45, "vi_name": "Miyazaki"},
	"鹿児島県":{"ja_name": "鹿児島県", "prefecture_id": 46, "vi_name": "Kagoshima"},
	"沖縄県":{"ja_name": "沖縄県", "prefecture_id": 47, "vi_name": "Okinawa"}
}
#############################################
def string2IntList(stringList):
	resultList = []
	for i in xrange(len(stringList)):
		resultList.append(int(stringList[i]))
	return resultList

def readSoup(url):
	response = br.open(url)
	soup = BeautifulSoup(response, 'lxml')
	return soup
##############################################
def treatJC(soup, ja_name):
	data = {}
	tables = soup.find_all('table', {'class': 'tableStyle04'})
	############################################
	data["uploaded_time"] = "2015-08"
	#############################################
	title = soup.find('h2')
	data["hira_name"] = title.span.text.strip()
	data["ja_name"] = ja_name
	data["en_name"] = soup.find('p').text.strip()
	############################################
	code = soup.find('div', {'class': 'floL'})
	data["code"] = code.text.strip()[4:][:-9].strip()
	############################################
	mini_tables = tables[0].find_all('table')
	mini_table_1 = mini_tables[0].find_all('tr')
	data["address"] = mini_table_1[0].td.find_all('span')[2].text.strip()
	##################################
	for prefecture in prefectureDict.keys():
		if prefecture.decode("utf-8") in data["address"]:
			data["prefecture"] = {}
			data["prefecture"]["ja_name"] = prefectureDict[prefecture]["ja_name"]
			data["prefecture"]["prefecture_id"] = prefectureDict[prefecture]["prefecture_id"]
			data["prefecture"]["vi_name"] = prefectureDict[prefecture]["vi_name"]
	##################################
	data["postal"] = mini_table_1[0].td.find_all('span')[1].text.strip()
	data["tel"] = mini_table_1[1].find_all('td')[1].text.strip()
	data["stations"] = mini_table_1[1].find_all('td')[2].text.strip()[9:].strip().split('、'.decode("utf-8"))
	data["fax"] = mini_table_1[2].find_all('td')[1].text.strip()
	data["homepage"] = mini_table_1[3].find_all('td')[1].text.strip()
	data["email"] = mini_table_1[4].find_all('td')[1].text.strip()
		#########
		#mini_tables[1]
	mini_table_1 = mini_tables[1].find_all('tr')
	data["personnel"] = mini_table_1[0].find_all('td')[1].text.strip()
	data["establishment"] = mini_table_1[0].find_all('td')[3].text.strip().replace('年'.decode("utf-8"),'-').replace('月'.decode("utf-8"),'-').replace('日'.decode("utf-8"),'')
	data["personnel_type"] = mini_table_1[1].find_all('td')[1].text.strip()
	qualification = mini_table_1[1].find_all('td')[3].text.strip().split('～'.decode("utf-8"))
	data["qualification_start"] = qualification[0].strip().replace('年'.decode("utf-8"),'-').replace('月'.decode("utf-8"),'-').replace('日'.decode("utf-8"),'')
	data["qualification_end"] = qualification[1].strip().replace('年'.decode("utf-8"),'-').replace('月'.decode("utf-8"),'-').replace('日'.decode("utf-8"),'')
	data["representative"] = mini_table_1[2].find_all('td')[1].text.strip()
	try:
		teacher = mini_table_1[2].find_all('td')[3].text.strip().split('（'.decode("utf-8"))
		data["teacher_number"] = int(teacher[0].strip()[:-1].strip())
		data["fulltime_teacher"] = int(teacher[1].strip()[5:][:-2].strip())
	except:
		data["teacher_number"] = int(mini_table_1[2].find_all('td')[3].text.strip())
		data["fulltime_teacher"] = None
	data["principal"] = mini_table_1[3].find_all('td')[1].text.strip()
	try:
		quota = mini_table_1[3].find_all('td')[3].text.strip().split('('.decode("utf-8"))
		data["quota"] = int(quota[0].strip()[:-1].strip()[:-1])
		data["quota_type"] = quota[1].strip()[:-1].strip()
	except:
		data["quota"] = int(mini_table_1[3].find_all('td')[3].text.strip()[:-1])
		data["quota_type"] = None
	data["education_act"] = mini_table_1[4].find_all('td')[1].text.strip()
	data["dormitory"] = {}
	dormitory = mini_table_1[4].find_all('td')[3].text.strip()
	if dormitory[0] == "有".decode("utf-8"):
		dormitory = dormitory[1:].strip()
		data["dormitory"]["has_dormitory"] = True
		try:
			price = dormitory.split('円'.decode("utf-8"))[0].strip()
			if '〜'.decode("utf-8") in price:
				price_list = price.split('〜'.decode("utf-8"))
				data["dormitory"]["dormitory_price"] = {}
				try:
					data["dormitory"]["dormitory_price"]["min"] = int(price_list[0].strip().replace(','.decode("utf-8"), ''))
					data["dormitory"]["dormitory_price"]["max"] = int(price_list[1].strip().replace(','.decode("utf-8"), ''))
				except:
					data["dormitory"]["dormitory_price"]["max"] = None
			else:
				data["dormitory"]["dormitory_price"] = int(price.replace(','.decode("utf-8"), ''))
		except:
			data["dormitory"]["dormitory_price"] = 0
	else:
		data["dormitory"]["has_dormitory"] = False
		data["dormitory"]["dormitory_price"] = 0
		###########
		#mini_tables[2]
	mini_table_1 = mini_tables[2].find_all('tr')
	data["entrance_qualification"] = mini_table_1[0].find_all('td')[1].text.strip()
	data["admission"] = mini_table_1[1].find_all('td')[1].text.strip().split('、'.decode("utf-8"))
	############
	#table[1]
	data["student_countries"] = []
	table_line = tables[1].find_all('tr')
	try:
		data["non_student_number"] = int(table_line[-1].td.text.strip())
	except:
		data["non_student_number"] = 0
	for i in xrange(len(table_line)-1):
		country = table_line[i].find_all('td')
		for col in country:
			_data = {}
			_string = col.text.strip().split('\n')
			_data["country_ja"] = _string[0].strip()
			# if _data["country_ja"] in country_code.keys():
			# 	_data["country_vi"] = country_code[_data["country_ja"]]["vi"]
			# 	_data["country_code"] = country_code[_data["country_ja"]]["code"]
			_data["number"] = int(_string[1].strip())
			if _data["country_ja"] != "合計".decode("utf-8"):
				data["student_countries"].append(_data)
			else:
				data["student_number"] = _data["number"]
	###################
	#table[2]
	data["courses"] = []
	table_line = tables[2].find_all('tr')
	try:
		data["other_courses"] = table_line[-1].td.text.strip().replace('('.decode("utf-8"), '_').replace(')'.decode("utf-8"), '_').replace('、'.decode("utf-8"), '_').split('_')
	except:
		data["other_courses"] = None
	for i in xrange(2, (len(table_line)-1)):
		_course = table_line[i].find_all('td')
		_data = {}
		try:
			_data["name"] = _course[0].text.strip()
			_data["purpose"] = _course[1].text.strip()
			_data["duration_year"] = _course[2].text.strip()
			if _data["duration_year"] == "1年9か月".decode("utf-8"):
				_data["duration_year"] = 1.75
			elif _data["duration_year"] == "1年6か月".decode("utf-8"):
				_data["duration_year"] = 1.5
			elif _data["duration_year"] == "1年3か月".decode("utf-8"):
				_data["duration_year"] = 1.25
			else:
				_data["duration_year"] = int(_data["duration_year"][:-1])
			_data["duration_hour"] = int(_course[3].text.strip().replace(','.decode("utf-8"), ''))
			_data["duration_week"] = int(_course[4].text.strip())
			_data["entrance_month"] = string2IntList(_course[5].text.strip().split(','.decode("utf-8")))
			_data["application_fee"] = int(_course[6].text.strip().replace(','.decode("utf-8"), ''))
			_data["admission_fee"] = int(_course[7].text.strip().replace(','.decode("utf-8"), ''))
			_data["tuition_fee"] = int(_course[8].text.strip().replace(','.decode("utf-8"), ''))
			_data["other_fee"] = int(_course[9].text.strip().replace(','.decode("utf-8"), ''))
			_data["total_fee"] = int(_course[10].text.strip().replace(','.decode("utf-8"), ''))
			data["courses"].append(_data)
		except:
			break
	# ######################
	#tableStyle03
	data["jlpt"] = {}
	data["jlpt"]["examinee"] = {}
	data["jlpt"]["accreditor"] = {}
	N_table = soup.find('table', {'class': 'tableStyle03'})
	table_line = N_table.find_all('tr')
	data["jlpt"]["examinee"]["N1"] = int(table_line[1].find_all('td')[0].text.strip())
	data["jlpt"]["examinee"]["N2"] = int(table_line[1].find_all('td')[1].text.strip())
	data["jlpt"]["examinee"]["N3"] = int(table_line[1].find_all('td')[2].text.strip())
	data["jlpt"]["examinee"]["N4"] = int(table_line[1].find_all('td')[3].text.strip())
	data["jlpt"]["examinee"]["N5"] = int(table_line[1].find_all('td')[4].text.strip())
	data["jlpt"]["accreditor"]["N1"] = int(table_line[2].find_all('td')[0].text.strip())
	data["jlpt"]["accreditor"]["N2"] = int(table_line[2].find_all('td')[1].text.strip())
	data["jlpt"]["accreditor"]["N3"] = int(table_line[2].find_all('td')[2].text.strip())
	data["jlpt"]["accreditor"]["N4"] = int(table_line[2].find_all('td')[3].text.strip())
	data["jlpt"]["accreditor"]["N5"] = int(table_line[2].find_all('td')[4].text.strip())
	# #########################
	#tables[3]
	data["eju"] = {"1st_round":{"japanese":{}, "art":{}, "science":{}}, "2nd_round":{"japanese":{}, "art":{}, "science":{}}}
	table_line = tables[3].find_all('tr')[-1].find_all('td')
	data["eju"]["1st_round"]["japanese"]["examinee"] = int(table_line[0].text.strip())
	data["eju"]["1st_round"]["japanese"]["over_219"] = int(table_line[1].text.strip())
	data["eju"]["1st_round"]["art"]["examinee"] = int(table_line[2].text.strip())
	data["eju"]["1st_round"]["art"]["over_100"] = int(table_line[3].text.strip())
	data["eju"]["1st_round"]["science"]["examinee"] = int(table_line[4].text.strip())
	data["eju"]["1st_round"]["science"]["over_100"] = int(table_line[5].text.strip())
	########
	data["eju"]["2nd_round"]["japanese"]["examinee"] = int(table_line[6].text.strip())
	data["eju"]["2nd_round"]["japanese"]["over_219"] = int(table_line[7].text.strip())
	data["eju"]["2nd_round"]["art"]["examinee"] = int(table_line[8].text.strip())
	data["eju"]["2nd_round"]["art"]["over_100"] = int(table_line[9].text.strip())
	data["eju"]["2nd_round"]["science"]["examinee"] = int(table_line[10].text.strip())
	data["eju"]["2nd_round"]["science"]["over_100"] = int(table_line[11].text.strip())
	# ##########################
	data["graduates_number"] = int(soup.find_all('span', {'class': 'lsp30'})[1].text.strip()[6:])
	#tables[4]
	data["go_higher"] = {}
	table_line = tables[4].find_all('tr')
	data["go_higher"]["graduation"] = int(table_line[1].find_all('td')[0].text.strip())
	data["go_higher"]["undergraduation"] = int(table_line[1].find_all('td')[1].text.strip())
	data["go_higher"]["junior_college"] = int(table_line[1].find_all('td')[2].text.strip())
	data["go_higher"]["professional_college"] = int(table_line[1].find_all('td')[3].text.strip())
	data["go_higher"]["vocational_school"] = int(table_line[1].find_all('td')[4].text.strip())
	data["go_higher"]["various_school"] = int(table_line[1].find_all('td')[5].text.strip())
	data["go_higher"]["other_school"] = int(table_line[1].find_all('td')[6].text.strip())
	data["go_higher"]["big_name"] = table_line[2].text.strip().replace('、'.decode("utf-8"), '-').replace('・'.decode("utf-8"), '-').split('-')
	# ############################
	#tables[5]
	data["features"] = {}
	table_line = tables[5].find_all('tr')
	for i in xrange(len(table_line)):
		try:
			data["features"][str(i+1)] = table_line[i].td.text.strip()
		except:
			continue
	############################################
	japCenter.insert_one(data)
	pass

if __name__ == '__main__':
	count = 1
	file_name = 'test.txt'
	f = codecs.open(file_name, 'r', 'utf-8')
	######################################
	for line in f:
		flag = line.find('http://')
		url = line[flag:]
		name = line[0:flag]
		print "=====================================>insert jc(s): ", count
		count += 1
		treatJC(readSoup(url), name)
	######################################
	f.close()