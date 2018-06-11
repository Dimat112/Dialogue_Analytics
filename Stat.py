import codecs
import re
import pandas
from Configuration import *

def main():
	ffile = codecs.open('WordStop.txt', 'r', encoding='utf8')
	try:
		stops = ffile.read()
	finally:
		ffile.close()

	# читаем файл
	ffile = codecs.open('messages_' + Friend_Name + '.txt', 'r', encoding='utf8')
	try:
		txt = ffile.read()
	finally:
		ffile.close()

	# выбираем слова через регулярные выражения
	res = re.findall('[А-Яа-я]+', txt, re.U)
	stopwords = re.findall('[А-Яа-я]+', stops, re.U)

	print ('Повторяющихся слов:', len(res))
	res = [x.lower() for x in res]
	res = pandas.Series([x for x in res if x not in stopwords and len(x) > 1])

	save_csv = pandas.DataFrame(res.value_counts(), columns = ['Count'])
	save_csv.to_csv("stat.csv", index_label='Word')
	print (res.value_counts())
	