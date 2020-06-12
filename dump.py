
import sqlite3



conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
f=open('data.txt','w')

cur.execute('SELECT html FROM Pages WHERE html is NOT NULL and error is NULL')
for i in range(0,20):
	row = cur.fetchone()#[i]	

	#print(row[0])
	if( type(row[0]) == type("str") ):
		f.write(row[0])
		f.write("\n\n\n\n")
	#else:
	#	f.write(row[0].decode("utf-8"))

