
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
