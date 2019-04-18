import pymysql

db = pymysql.connect("master", "root", "Hadoopc102*", "stock_portrait")

cursor = db.cursor()

def truncate_table(table=''):
	sql = 'truncate '+table
	cursor.execute(sql)


if __name__ == '__main__':
    truncate_table('stock_list')