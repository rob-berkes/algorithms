
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
	
	return


vals=factorBrute(90)
sumFactors(vals)
