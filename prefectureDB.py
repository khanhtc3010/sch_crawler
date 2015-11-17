# -*- coding: utf-8 -*-
import requests, codecs, mechanize
from pymongo import MongoClient
from bs4 import BeautifulSoup
#############################################
client = MongoClient('localhost', 27017) #connext to mongodb
db = client.japanesecenterDB	#create a database
japPrefecture = db.prefecture #create a collection
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
#######################################################
if __name__ == '__main__':
	for prefecture in prefectureDict.keys():
		data = {}
		########################################
		data["prefecture_id"] = prefectureDict[prefecture]["prefecture_id"]
		data["ja_name"] = prefectureDict[prefecture]["ja_name"]
		data["vi_name"] = prefectureDict[prefecture]["vi_name"]
		########################################
		japPrefecture.insert_one(data)