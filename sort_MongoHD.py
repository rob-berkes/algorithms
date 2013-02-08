from lib import sorting 
from multiprocessing import Process,Pipe,Queue
import random
import sys
if __name__ == '__main__' :
	sys.setrecursionlimit(2000)
	n=7  #number partitions to break into
	IFILE=open("/home/ec2-user/mongo.csv","r")
	SORTME=[]
	for line in IFILE:
		line=line.strip().split(',')
		rec=(line[0],line[1])
		SORTME.append(rec)
	IFILE.close()

	print 'done reading list .... starting mulitple procs'
	pconn,cconn=Pipe()
	lyst=[]
	p=Process(target=sorting.QuickSortMPListArray,args=(SORTME,cconn,n))
	p.start()
	print 'main proc started'

	lyst=pconn.recv()
	print 'starting out write'
	print 'joining child procs'
	p.join()
	OFILE=open("/home/ec2-user/mongo.csv.sorted","w")
	for a in lyst:
		OFILE.write(str(a)+'\n')
	OFILE.close()
	print 'all done!'
