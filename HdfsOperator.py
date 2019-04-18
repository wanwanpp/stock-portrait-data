from hdfs.client import Client
import tushare as ts
import pandas

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


def append_csv_to_hdfs_file(hdfs_path, data):
	with client.write(hdfs_path, encoding='utf-8') as writer:
		data.to_csv(writer, encoding='utf-8', index=False, header=False, mode='a')
