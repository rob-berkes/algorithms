import random

def factorBrute(A):
	n=2
	newmax=A
	vals=[1,]
	count=0
	for n in range(2,newmax):
		count+=1
		if A % n == 0:
			vals.append(n)
			newmax=int(A/n)

	print vals
	return vals,count

def sumFactors(vals):
	factorSum=0
	for a in vals:
		factorSum+=a	
	return factorSum


def QuickSort(A,Depth):
	Depth+=1
	if len(A)==1:
		print "return from Depth "+str(Depth)+" , values "+str(A)
		return A
	elif len(A)==0:
		print "return from Depth "+str(Depth)+" , values "+str(A)
		return A
	else:
		PartIndex=random.randint(0,len(A)-1)
		PartitionValue=A.pop(PartIndex)
		lesser=[]
		greater=[]
		for val in range(0,len(A)):
			if A[val] <= PartitionValue:
				lesser.append(A[val])
			else:
				greater.append(A[val])
		print 'Depth: '+str(Depth)+' Lesser: '+str(lesser)+' Greater: '+str(greater)+ ' PartVal: '+str(PartitionValue)
		pv=[]
		pv.append(PartitionValue)
	return QuickSort(lesser,Depth)+pv+QuickSort(greater,Depth)			

def BubbleSort(A):
	swap_done=True
	while swap_done:
		swap_done=False
		for valu in range(0,len(A)-1):
			if A[valu] > A[valu+1]:
				swap_done=True
				t=A[valu+1]
				A[valu+1]=A[valu]
				A[valu]=t

	return A

#numArray=[33550336,10000000,10000001,10000233,]
SORTME=[99,24,88,77,66,111,1,22,44,33,55,]
SORTME+=[3,6,4,2,7,22,635,23,78,99,642,22,99,123,55,66,88,21,3,3,13,31,41,14,51,61,161,15,14,16,88,999,1234,555,777,888,999,]
SORTME+=[1,8,3,3,2,5,]
SORTME+=[2,2,1,]
print SORTME
#for item in range(0,len(SORTME)-1):
#SORTME=QuickSort(SORTME,1)
BubbleSort(SORTME)
print SORTME
#for NUMBER in range(200000000,200000100):
#	vals=factorBrute(NUMBER)
#	if sumFactors(vals)==NUMBER:
#		print "Perfect number! Sum of "+str(NUMBER)+" is "+str(sumFactors(vals))
#	elif sumFactors(vals)==1:
#		print "Prime number! "+str(NUMBER)+"'s factor sum is 1"
#	else:
#		print "non perfect, sum of "+str(NUMBER)+"'s factors is "+str(sumFactors(vals))
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
