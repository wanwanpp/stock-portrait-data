import tushare as ts
import pymysql

pro = ts.pro_api('4d7357aee9bef99c3b5d61f37a3451535f4cdd6a63fe45e3b0080c4e')

# db = pymysql.connect("localhost", "root", "wp980325", "stock_portrait")
db = pymysql.connect("master", "root", "Hadoopc102*", "stock_portrait")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

execute_count = 0

def get_trade_calendar():
	trade_cal = pro.trade_cal(exchange='', start_date='20160101')
	return trade_cal

def create_table():
	create_sql ="""CREATE TABLE trade_calendar (id int not null primary key auto_increment, exchange  varchar(20), cal_date  varchar(50), is_open int )"""
	print(cursor.execute(create_sql))


def insert_data(exchange=None, cal_date=None, is_open=None):
	global execute_count
	sql = "INSERT INTO trade_calendar(exchange, \
	       cal_date, is_open) \
	       VALUES ('%s', '%s',  %s)" % \
		  (exchange, cal_date, is_open)
	
	try:
		cursor.execute(sql)
		db.commit()
		execute_count = execute_count+1
		print(execute_count)
	except:
		db.rollback()


def select_isopen_by_caldate(cal_date):
	sql = "select is_open from trade_calendar where cal_date='%s'" % cal_date
	cursor.execute(sql)
	result = cursor.fetchall()
	return result[0][0]

if __name__ == '__main__':

	# create_table()

	# trade_cal = get_trade_calendar()
	# print(trade_cal.shape)
	# for index,row in trade_cal.iterrows():
	# 	insert_data(row[-3],row[-2],row[-1])
	# print(execute_count)
	# db.close()

	result = select_isopen_by_caldate('20190422')
	print(result==1)
