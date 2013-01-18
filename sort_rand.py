from lib import sorting 
from multiprocessing import Pool,Manager







if __name__ == '__main__' :
	pool=Pool(processes=4)
	manager=Manager()
	SORTME=[9,4,3,5,8,11,234,22,2355,78,3,99,4,788,]
#	IFILE=open('rand.list','r')
#	for line in IFILE:
#	        SORTME.append(int(line))
#	IFILE.close()
	SME=manager.dict()
	SME=SORTME
	
	#NEWSORT=sorting.QuickSort(SME)

	#print NEWSORT
	#NEWSORT=sorting.BubbleSort(SORTME)
	res=pool.apply_async(sorting.QuickSort,SME)
	while pool.is_alive():
		pass
	RESULT=res.get()
	print RESULT
	print SME
	#print res
#	NEWSORT=res.get(timeout=10)
#	print NEWSORT
#	OFILE=open('rand.sorted','w')
#	OFILE.write(NEWSORT)
#	for a in NEWSORT:
#	        OFILE.write(str(a)+'\n')
#	OFILE.close()

