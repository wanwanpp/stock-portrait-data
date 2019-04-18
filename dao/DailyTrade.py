import time
import tushare as ts

pro = ts.pro_api('4d7357aee9bef99c3b5d61f37a3451535f4cdd6a63fe45e3b0080c4e')


def get_daily_trade_to_csv(start_date='', end_date='', file_save_path=''):
	trade_cal = get_trade_cal(start_date, end_date)
	write_count = 0
	for index, row in trade_cal.iterrows():
		if write_count == 0:
			mode = 'w'
		else:
			mode = 'a'
		if row[-1] == 1:
			write_count += 1
			daily = pro.daily(trade_date=row[-2])
			print(row[-2])
			daily.to_csv(file_save_path, encoding='utf-8', index=False, header=False, mode=mode)


def get_dailt_trade_util_today(start_date='', file_save_path=''):
	now = time.strftime("%Y%m%d", time.localtime())
	get_daily_trade_to_csv(start_date, now, file_save_path)


def get_trade_cal(start_date='', end_date=''):
	return pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)


# 获取某天的日交易数据
def get_oneday_trade(date=''):
	return pro.daily(trade_date=date)


if __name__ == '__main__':
	# get_today_trade()
	print(get_oneday_trade('20190417'))
