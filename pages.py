import sqlite3



conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('SELECT html,id FROM Pages WHERE html is NOT NULL and error is NULL')
for i in range(0,5):
	row = cur.fetchone()#[0]
	#print(row[1])
	name = str(row[1])
	name=name+".txt"
	f=open(name,'w')
 #  	name=name+".txt"
 #  	f=open(name,'w')

	# # #print(row[0])
	if( type(row[0]) == type("str") ):
		
		f.write(row[0])
		f.write("\n\n\n\n")
	#else:
	#	f.write(row[0].decode("utf-8"))
