import sys
from hdfs.client import Client

client = Client("http://172.23.253.80:50070/", root="/", timeout=10000, session=False)


def upload(hdfs_path='', local_file_path='', cleanup=True):
	return client.upload(hdfs_path, local_file_path, cleanup)


def delete_hdfs_file(hdfs_path):
	return client.delete(hdfs_path)


if __name__ == '__main__':
	# delete_succeed = delete_hdfs_file('/a.txt')
	# print(delete_succeed)
	upload_succeed = upload('/', 'C:\\Users\\wanwanpp\\Desktop\\a.txt')
	print(upload_succeed)