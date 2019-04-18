import time

import tushare as ts

# today_trade_data=ts.get_day_all('2019-03-29')
# today_trade_data=ts.get_day_all('2019-04-01')
# # today_trade_data.to_csv('/root/tushare/20190401/daytrade_data.csv')
# # today_trade_data.to_csv('E:\PythonProject\stockPortrait\daytrade_data.csv', encoding='utf-8', index=False,header=False)
# print(today_trade_data)
# today_trade_data.describe

pro = ts.pro_api('4d7357aee9bef99c3b5d61f37a3451535f4cdd6a63fe45e3b0080c4e')
# df = pro.daily(trade_date='20190401')
# print(df)
# print(pro.daily(trade_date='20190402'))
# pro.query()
# print(pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date'))
now = time.strftime("%Y%m%d", time.localtime())
trade_cal = pro.trade_cal(exchange='', start_date='20190101',end_date=now)
# print(trade_cal)
write_count=0
for index,row in trade_cal.iterrows():
	# print(rowa)
	#print(row[-1],row[-2])
	if write_count==0:
		mode = 'w'
	else:
		mode = 'a'
	if row[-1]==1:
		write_count+=1
		daily=pro.daily(trade_date=row[-2])
		print(row[-2])
		daily.to_csv('E:\PythonProject\stockPortrait\daytrade_data.csv', encoding='utf-8', index=False,header=False,mode=mode)



# today_trade_data=pd.read_csv('/root/tushare/20190401/daytrade_data.csv',index_col='code')
# today_trade_data.drop([ 'Unnamed: 0'],axis=1,inplace=True)
# today_trade_data.to_csv('/root/tushare/20190401/result.csv')
# print(today_trade_data)
# print(today_trade_data.describe())

