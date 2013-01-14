from lib import sorting 
from lib import factoring 



SORTME=[]
#numArray=[33550336,10000000,10000001,10000233,]
#SORTME=[99,24,88,77,66,111,1,22,44,33,55,]
#SORTME+=[3,6,4,2,7,22,635,23,78,99,642,22,99,123,55,66,88,21,3,3,13,31,41,14,51,61,161,15,14,16,88,999,1234,555,777,888,999,]
#SORTME+=[1,8,3,3,2,5,]
#SORTME=[2,2,1,]
#print SORTME
#IFILE=open('rand.list','r')
#for line in IFILE:
#	SORTME.append(int(line))
#IFILE.close()
#for item in range(0,len(SORTME)-1):
#SORTME=QuickSort(SORTME,1)


#NEWSORT=sorting.QuickSort(SORTME)
#NEWSORT=sorting.BubbleSort(SORTME)





#print SORTME
#OFILE=open('rand.sorted','w')
#for a in NEWSORT:
#	OFILE.write(str(a)+'\n')
#OFILE.close()

OFILE=open('output.factorsums','w')
for NUMBER in range(0,2015):
	vals,count=factoring.factorBrute(NUMBER)
	OFILE.write(str(NUMBER)+' '+str(factoring.sumFactors(vals))+'\n')
#	if sumFactors(vals)==NUMBER:
#		pass
#		print "Perfect number! Sum of "+str(NUMBER)+" is "+str(sumFactors(vals))
#	elif sumFactors(vals)==1:
#		print "Prime number! "+str(NUMBER)+"'s factor sum is 1"
#	else:
#		pass
#		print "non perfect, sum of "+str(NUMBER)+"'s factors is "+str(sumFactors(vals))

OFILE.close()

#NUMBER=4096
#numArray=[7,6,28,100,8128,256,512,1024,33550336]
#for NUMBER in numArray:
#	vals,count=factorBrute(NUMBER)
#	if sumFactors(vals)==NUMBER:
#		print "("+str(count)+") Perfect number! Sum of "+str(NUMBER)+" is "+str(sumFactors(vals))
#	elif sumFactors(vals)==1:
#		print "("+str(count)+") Prime number! "+str(NUMBER)+"'s factor sum is 1"
#	else:
#		print "("+str(count)+") non perfect, sum of "+str(NUMBER)+"'s factors is "+str(sumFactors(vals))
