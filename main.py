
def factorBrute(A):
	n=2
	newmax=A
	vals=[1,]
	for n in range(2,newmax):
		if A % n == 0:
			vals.append(n)
			newmax=int(A/n)

	print vals
	return vals

def sumFactors(vals):
	factorSum=0
	for a in vals:
		factorSum+=a	
	return factorSum



NUMBER=4096
numArray=[7,6,28,100,8128,256,512,1024,33550336]
for NUMBER in numArray:
	vals=factorBrute(NUMBER)
	if sumFactors(vals)==NUMBER:
		print "Perfect number! Sum of "+str(NUMBER)+" is "+str(sumFactors(vals))
	elif sumFactors(vals)==1:
		print "Prime number! "+str(NUMBER)+"'s factor sum is 1"
	else:
		print "non perfect, sum of "+str(NUMBER)+"'s factors is "+str(sumFactors(vals))
