
import sqlite3



conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('SELECT html,id FROM Pages WHERE html is NOT NULL and error is NULL')
for i in range(0,20):
	row = cur.fetchone()[0]
  name= cur.fetchone()[1]
  name=name+".txt"
  f=open(name,'w')

	#print(row[0])
	if( type(row[0]) == type("str") ):
		s=row[0]
		u = unicode(s, "utf-8")
		f.write(u)
		f.write("\n\n\n\n")
	#else:
	#	f.write(row[0].decode("utf-8"))

