#coding: utf-8
import codecs, sys

def refineCountry(data):
	return data\
	.replace("\"中国\"".decode("utf-8"),"\"中国\",\"country_vi\":\"Trung Quốc\",\"code\":\"CN\"".decode("utf-8"))\
	.replace("\"韓国\"".decode("utf-8"), "\"韓国\",\"country_vi\":\"Hàn Quốc\",\"code\":\"KP\"".decode("utf-8"))\
	.replace("\"台湾\"".decode("utf-8"), "\"台湾\",\"country_vi\":\"Đài Loan\",\"code\":\"TW\"".decode("utf-8"))\
	.replace("\"ﾍﾞﾄﾅﾑ\"".decode("utf-8"), "\"ﾍﾞﾄﾅﾑ\",\"country_vi\":\"Việt Nam\",\"code\":\"VN\"".decode("utf-8"))\
	.replace("\"ﾈﾊﾟｰﾙ\"".decode("utf-8"), "\"ﾈﾊﾟｰﾙ\",\"country_vi\":\"Nepal\",\"code\":\"NP\"".decode("utf-8"))\
	.replace("\"ﾀｲ\"".decode("utf-8"), "\"ﾀｲ\",\"country_vi\":\"Thái Lan\",\"code\":\"TH\"".decode("utf-8"))\
	.replace("\"ﾐｬﾝﾏｰ\"".decode("utf-8"), "\"ﾐｬﾝﾏｰ\",\"country_vi\":\"Myanmar\",\"code\":\"MM\"".decode("utf-8"))\
	.replace("\"ﾓﾝｺﾞﾙ\"".decode("utf-8"), "\"ﾓﾝｺﾞﾙ\",\"country_vi\":\"Mông Cổ\",\"code\":\"MN\"".decode("utf-8"))\
	.replace("\"ｲﾝﾄﾞﾈｼｱ\"".decode("utf-8"), "\"ｲﾝﾄﾞﾈｼｱ\",\"country_vi\":\"Indonesia\",\"code\":\"RI\"".decode("utf-8"))\
	.replace("\"ｽﾘﾗﾝｶ\"".decode("utf-8"), "\"ｽﾘﾗﾝｶ\",\"country_vi\":\"Sri Lanka\",\"code\":\"LK\"".decode("utf-8"))\
	.replace("\"ｽｳｪｰﾃﾞﾝ\"".decode("utf-8"), "\"ｽｳｪｰﾃﾞﾝ\",\"country_vi\":\"Thụy Điển\",\"code\":\"SE\"".decode("utf-8"))\
	.replace("\"ﾏﾚｰｼｱ\"".decode("utf-8"), "\"ﾏﾚｰｼｱ\",\"country_vi\":\"Malaysia\",\"code\":\"MY\"".decode("utf-8"))\
	.replace("\"ｱﾒﾘｶ\"".decode("utf-8"), "\"ｱﾒﾘｶ\",\"country_vi\":\"Mỹ\",\"code\":\"US\"".decode("utf-8"))\
	.replace("\"ｲﾝﾄﾞ\"".decode("utf-8"), "\"ｲﾝﾄﾞ\",\"country_vi\":\"Ấn Độ\",\"code\":\"IN\"".decode("utf-8"))\
	.replace("\"ﾌﾗﾝｽ\"".decode("utf-8"), "\"ﾌﾗﾝｽ\",\"country_vi\":\"Pháp\",\"code\":\"FR\"".decode("utf-8"))\
	.replace("\"ﾛｼｱ\"".decode("utf-8"), "\"ﾛｼｱ\",\"country_vi\":\"Nga\",\"code\":\"RU\"".decode("utf-8"))\
	.replace("\"ﾌｨﾘﾋﾟﾝ\"".decode("utf-8"), "\"ﾌｨﾘﾋﾟﾝ\",\"country_vi\":\"Philippin\",\"code\":\"PI\"".decode("utf-8"))\
	.replace("\"ｻｳｼﾞｱﾗﾋﾞｱ\"".decode("utf-8"), "\"ｻｳｼﾞｱﾗﾋﾞｱ\",\"country_vi\":\"Saudi Arabia\",\"code\":\"SA\"".decode("utf-8"))\
	.replace("\"ｲﾀﾘｱ\"".decode("utf-8"), "\"ｲﾀﾘｱ\",\"country_vi\":\"Italia\",\"code\":\"IT\"".decode("utf-8"))\
	.replace("\"ｽﾍﾟｲﾝ\"".decode("utf-8"), "\"ｽﾍﾟｲﾝ\",\"country_vi\":\"Tây Ban Nha\",\"code\":\"ES\"".decode("utf-8"))\
	.replace("\"ｲｷﾞﾘｽ\"".decode("utf-8"), "\"ｲｷﾞﾘｽ\",\"country_vi\":\"Anh\",\"code\":\"UK\"".decode("utf-8"))\
	.replace("\"ｶﾅﾀﾞ\"".decode("utf-8"), "\"ｶﾅﾀﾞ\",\"country_vi\":\"Canada\",\"code\":\"CA\"".decode("utf-8"))\
	.replace("\"ﾊﾞﾝｸﾞﾗﾃﾞｼｭ\"".decode("utf-8"), "\"ﾊﾞﾝｸﾞﾗﾃﾞｼｭ\",\"country_vi\":\"Bangladesh\",\"code\":\"BD\"".decode("utf-8"))\
	.replace("\"ｶﾝﾎﾞｼﾞｱ\"".decode("utf-8"), "\"ｶﾝﾎﾞｼﾞｱ\",\"country_vi\":\"Cam-pu-chia\",\"code\":\"KH\"".decode("utf-8"))\
	.replace("\"ｼﾝｶﾞﾎﾟｰﾙ\"".decode("utf-8"), "\"ｼﾝｶﾞﾎﾟｰﾙ\",\"country_vi\":\"Shingapo\",\"code\":\"SG\"".decode("utf-8"))\
	.replace("\"ｽｲｽ\"".decode("utf-8"), "\"ｽｲｽ\",\"country_vi\":\"Thụy Sĩ\",\"code\":\"CH\"".decode("utf-8"))\
	.replace("\"ﾄﾞｲﾂ\"".decode("utf-8"), "\"ﾄﾞｲﾂ\",\"country_vi\":\"Đức\",\"code\":\"DE\"".decode("utf-8"))\
	.replace("\"ｵｰｽﾄﾗﾘｱ\"".decode("utf-8"), "\"ｵｰｽﾄﾗﾘｱ\",\"country_vi\":\"Úc\",\"code\":\"AU\"".decode("utf-8"))

def refineBigName(data):
	return data.replace("主な進学先：\n".decode("utf-8"), "")

if __name__ == '__main__':
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	f = codecs.open(inputFile, "r", "utf-8")
	f1 = codecs.open(outputFile, "a", "utf-8")
	##########################################
	for line in f:
		_data = refineCountry(line)
		f1.write(_data)
	##########################################
	f.close()
	f1.close()