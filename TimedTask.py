import os
import logging
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def config_logging():
	LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
	logging.basicConfig(filename='../python-log/timedTask.log', level=logging.DEBUG, format=LOG_FORMAT)


def tick():
	print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':

	config_logging()
	logging.info("starting timed task")
	scheduler = BlockingScheduler()
	scheduler.add_job(tick, 'cron', hour=16, minute=1)

	print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

	try:
		scheduler.start()
		logging.info('timed task start successfully')
	except (KeyboardInterrupt, SystemExit):
		# except BaseException as e:
		logging.error('timed task shutdown', exc_info=True)
		pass
