import sys

import hdfs
from hdfs.client import Client
import tushare as ts
import pandas
import csv

test_trade_data = ts.get_day_all('2019-03-29')

client = Client("http://172.23.253.80:50070/", root="/", timeout=10000, session=False)


def upload(hdfs_path='', local_file_path='', cleanup=True):
	return client.upload(hdfs_path, local_file_path, cleanup)


def delete_hdfs_file(hdfs_path):
	return client.delete(hdfs_path)


def read_csv_from_hdfs(hdfs_path):
	with client.read(hdfs_path, encoding='utf-8') as reader:
		csv = pandas.read_csv(reader)
		return csv


if __name__ == '__main__':
	# dataframe以csv格式写入HDFS中
	# with client.write('/a.csv', encoding='utf-8') as writer:
	# 	test_trade_data.to_csv(writer)

	delete_hdfs_file('stock_portrait')

	# csv = read_csv_from_hdfs('/a.csv')
	# print(type(csv))
	# print(csv)
