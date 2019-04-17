import DailyTrade
import HdfsOperator

save_file_path = 'E:\PythonProject\stockPortrait\daytrade_data.csv'
start_date = '20190101'

if __name__ == '__main__':
	DailyTrade.get_dailt_trade_util_today(start_date, save_file_path)
	print(HdfsOperator.upload('/stock_portrait/', save_file_path, cleanup=True))
	# print(hdfsOperator.delete_hdfs_file('/a.txt'))