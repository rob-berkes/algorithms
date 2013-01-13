
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

<<<<<<< HEAD
	return vals
=======
	print vals
	return vals,count
>>>>>>> fdf5a3aaa869512e23a2e7fed822e96be5a05a9d

def sumFactors(vals):
	factorSum=0
	for a in vals:
		factorSum+=a	
	return factorSum

def qs_LtoR(ARRAY1,partItem,Index):
	truetocontinue=True
	COUNTER=Index
	print '<ltoR> Counter:'+str(COUNTER)
	while truetocontinue:
		try:
			if ARRAY1[COUNTER+1] < partItem:
				COUNTER+=1
			else:
				truetocontinue=False
		except IndexError:
			COUNTER+=1
			truetocontinue=False
	print '<ltoR-2> Counter:'+str(COUNTER)

	return COUNTER
	
def qs_RtoL(ARRAY1,partItem,Index):
	truetocontinue=True
	COUNTER=Index
	while truetocontinue:
		if ARRAY1[COUNTER-1] > partItem:
			COUNTER-=1
		else:
			COUNTER-=1
			truetocontinue=False
	return COUNTER
	
def qs_exchange(A1,l,r):
	print A1,l,r
	temp=A1[l]
	A1[l]=A1[r]
	A1[r]=temp
	print A1,l,r
	return A1

<<<<<<< HEAD
def QuickSort(A,Index):
	print '<qs> '+str(A)+str(Index)+'=Index, Val='+str(A[Index])
	lPos=qs_LtoR(A,A[Index],Index)
	rPos=qs_RtoL(A,A[Index],len(A)-1)
	A1=A
	if lPos < rPos :
		A1=qs_exchange(A,lPos,rPos)
			
	return A1

numArray=[33550336,10000000,10000001,10000233,]

SORTME=[3,6,4,2,7,22,635,23,78,99,642,22,99,123,55,66,88,21,3,3,13,31,41,14,51,61,161,15,14,16,88,999,1234,555,777,888,999,]
print SORTME
for item in range(0,len(SORTME)-1):
	print item
	SORTME=QuickSort(SORTME,item)
print SORTME
#for NUMBER in range(200000000,200000100):
#	vals=factorBrute(NUMBER)
#	if sumFactors(vals)==NUMBER:
#		print "Perfect number! Sum of "+str(NUMBER)+" is "+str(sumFactors(vals))
#	elif sumFactors(vals)==1:
#		print "Prime number! "+str(NUMBER)+"'s factor sum is 1"
#	else:
#		print "non perfect, sum of "+str(NUMBER)+"'s factors is "+str(sumFactors(vals))
=======
NUMBER=4096
numArray=[7,6,28,100,8128,256,512,1024,33550336]
for NUMBER in numArray:
	vals,count=factorBrute(NUMBER)
	if sumFactors(vals)==NUMBER:
		print "("+str(count)+") Perfect number! Sum of "+str(NUMBER)+" is "+str(sumFactors(vals))
	elif sumFactors(vals)==1:
		print "("+str(count)+") Prime number! "+str(NUMBER)+"'s factor sum is 1"
	else:
		print "("+str(count)+") non perfect, sum of "+str(NUMBER)+"'s factors is "+str(sumFactors(vals))
>>>>>>> fdf5a3aaa869512e23a2e7fed822e96be5a05a9d
