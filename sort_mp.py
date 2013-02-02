from lib import sorting 
from multiprocessing import Process,Pipe
import random
import pdb
if __name__ == '__main__' :
#	SORTME=[9,4,3,5,8,11,234,22,2355,78,3,99,4,788,100,22,234,34442,1,55,666,4478,85,332,7712,2,4,777,5,]
	SORTME=[random.random() for x in range(10000)]
	n=3  #proc to start
	pconn,cconn=Pipe()
	lyst=list(SORTME)
#	pdb.set_trace()
	p=Process(target=sorting.QuickSortMP,args=(lyst,cconn,n))
	p.start()
	lyst=pconn.recv()
	p.join()
	print lyst
