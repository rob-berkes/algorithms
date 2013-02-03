from pymongo import Connection

conn=Connection()
db=conn.wc

RESULTSET=db.hits.find()

OFILE=open('/home/ec2-user/hits.list.tmp','w')
for a in RESULTSET:
	OFILE.write(str(a['Hits'])+" # "+str(a['_id'])+" # "+str(a['title']))

OFILE.close()

