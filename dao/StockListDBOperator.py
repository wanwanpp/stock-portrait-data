import tushare as ts
import pymysql
import logging

pro = ts.pro_api('4d7357aee9bef99c3b5d61f37a3451535f4cdd6a63fe45e3b0080c4e')

# db = pymysql.connect("localhost", "root", "wp980325", "stock_portrait")
db = pymysql.connect("master", "root", "Hadoopc102*", "stock_portrait")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

execute_count = 0


def get_stock_basic():
	stock_basic = pro.stock_basic()
	return stock_basic


def insert_data(ts_code, symbol, name, area, industry, market, list_date):
	global execute_count
	sql = "INSERT INTO stock_list(ts_code, symbol, name, area, industry, market, list_date) \
	       VALUES ('%s', '%s',  '%s', '%s', '%s',  '%s', '%s')" % \
		  (ts_code, symbol, name, area, industry, market, list_date)

	try:
		cursor.execute(sql)
		db.commit()
		execute_count = execute_count + 1
		print(execute_count)
	except BaseException:
		logging.exception("error:")
		db.rollback()


def get_stock_basic_and_insert():
	stock_basic = get_stock_basic()
	print(stock_basic.shape)
	for index, row in stock_basic.iterrows():
		insert_data(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
	print(execute_count)
	# db.close()


if __name__ == '__main__':
	# create_table()

	get_stock_basic_and_insert()
# db.close()
