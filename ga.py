import random
class __CHROMO__:
	def __init__(self):
		value1=random.randint(0,10)+5.0
		value2=random.randint(0,10)-5.0
		score=0
	score=0


POPULATION=2000

FULLRAY=[]

def initRay():
	v1=random.randint(0,10)+5.0
	v2=random.randint(0,10)-5.0
	return	v1,v2

for a in range(0,2):
	v1,v2=initRay()
	print v1,v2
	FULLRAY.append(__CHROMO__())

print FULLRAY[0]('value1')
