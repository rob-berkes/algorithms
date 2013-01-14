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

#       print vals
        return vals,count

def sumFactors(vals):
        factorSum=0
        for a in vals:
                factorSum=factorSum+a
        return factorSum

