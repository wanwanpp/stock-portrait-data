import os
import logging
import time
from apscheduler.schedulers.blocking import BlockingScheduler

from DailyTrade import get_oneday_trade
from HdfsOperator import append_csv_to_hdfs_file
import TradeCaculateDBOperator as trade_cal_db
from util import MysqlUtil

daily_trade_file_path = '/stock_portrait/day_trade_data.csv'
stock_list = 'stock_list'
trade_calendar = 'trade_calendar'


def config_logging():
	LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
	logging.basicConfig(filename='../python-log/timedTask.log', level=logging.DEBUG, format=LOG_FORMAT)


def task():
	logging.info("begin to update daily trade info")
	# 1. 判断当天是否为交易日
	is_open = trade_cal_db.select_isopen_by_caldate('20190422')
	is_trading = (is_open == 1)
	if is_trading:
		# 2. 获取当天日交易数据
		now = time.strftime("%Y%m%d", time.localtime())
		today_trade_data = get_oneday_trade(now)
		# 3. 将数据追加到Hdfs文件中
		append_csv_to_hdfs_file(daily_trade_file_path, today_trade_data)

	logging.info("begin to update table trade calendar info")
	# 1. truncate table trade_calendar
	MysqlUtil.truncate_table(trade_calendar)
	# 2. 重新获取数据并写入表中
	trade_cal_db.get_trade_calendar_and_insert()

	logging.info("begin to update table stock list info")
	# 1. truncate table stock_list
	MysqlUtil.truncate_table(stock_list)
	# 2. 重新获取数据并写入表中



if __name__ == '__main__':

	# config_logging()
	# logging.info("starting timed task")
	# scheduler = BlockingScheduler()
	# scheduler.add_job(task, 'cron', hour=16, minute=1)
	#
	# print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
	#
	# try:
	# 	scheduler.start()
	# 	logging.info('timed task start successfully')
	# except (KeyboardInterrupt, SystemExit):
	# 	# except BaseException as e:
	# 	logging.error('timed task shutdown', exc_info=True)
	# 	pass

	task()