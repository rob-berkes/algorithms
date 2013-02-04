from lib import sorting 
from multiprocessing import Process,Pipe,Queue
import random
import sys
if __name__ == '__main__' :
	sys.setrecursionlimit(2000)
	n=12  #number partitions to break into
#	SORTME=[9,4,3,5,8,11,234,22,2355,78,3,99,4,788,100,22,234,34442,1,55,666,4478,85,332,7712,2,4,777,5,]
	SORTME=[random.randint(0,9999999) for x in range(100)]
	OFILE=open("/home/ec2-user/hits.list","r")
#	OFILE=open("rand.list","r")
#	UNSORTLIST=[]
	print 'start reading list...'
	for line in OFILE:
	        line=line.strip().split(' # ')
	        UNSORTLIST.append(line)
	OFILE.close()
	print 'done reading list .... starting mulitple procs'
	pconn,cconn=Pipe()
	lyst=[]
	p=Process(target=sorting.QuickSortMPListArray,args=(UNSORTLIST,cconn,n))
	p.start()
	print 'main proc started'
	lyst=pconn.recv()
	print 'joining child procs'
	p.join()
	OFILE=open("/home/ec2-user/hits.sorted","w")
#	OFILE=open("rand.sorted","w")
	for a in lyst:
		OFILE.write(str(a)+'\n')
	OFILE.close()
	print 'all done!'
