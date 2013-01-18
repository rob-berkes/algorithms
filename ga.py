import random
class __CHROMO__:
	def __init__(self):
		return
	def __init__(self,v1,v2):
		value1=v1
		value2=v2
		return
	value1=random.randint(0,10)+5.0
	value2=random.randint(0,10)-5.0
	score=0


		
POPULATION=2000
GENERATIONS=50
FULLRAY=[]


# Equation: 8x^2-10x-3
def evalu(value1,value2):
	score1=((value1*value1)*4)+(value1*4)+2
	score2=((value2*value2)*4)-(value2*4)+2
	summa=abs(score1)+abs(score2)
	return summa
def InitVars():
	v1=random.random()*10+5.0
	v2=random.random()*10-5.0
	return v1,v2
def InitArray(FULLRAY,POPULATION):

	for a in range(0,POPULATION):
	#	FULLRAY.append(__CHROMO__())
		t=__CHROMO__(0,0)
		t.value1,t.value2=InitVars()
		t.score=0
		FULLRAY.append(t)
		FULLRAY[a].score=evalu(FULLRAY[a].value1,FULLRAY[a].value2)

	return
def CrossOver(b1,b2,v1,v2,modus):
	MU_RATE=0.0001
	if modus==0: 
		new1=(b1+v1)*MU_RATE
		new2=(b2+v2)*MU_RATE
	elif modus==1:
		new1=(b1+v2)*MU_RATE
		new2=(b2+v1)*MU_RATE
 	elif modus==2:
		new1=(b1-v1)*MU_RATE
		new2=(b2-v2)*MU_RATE
	elif modus==3:
		new1=(b1-v2)*MU_RATE
		new2=(b2-v1)*MU_RATE
 	elif modus==4:
		new1=(b1+v1)*MU_RATE
		new2=(b2-v2)*MU_RATE
	elif modus==5:
		new1=(b1-v1)*MU_RATE
		new2=(b2+v2)*MU_RATE
 	elif modus==6:
		new1=(b1+v2)*MU_RATE
		new2=(b2+v1)*MU_RATE
	elif modus== 7:
		new1=(b1-v2)*MU_RATE
		new2=(b2+v1)*MU_RATE
	return new1,new2
def findBest(FULLRAY):
	IndexBest=0
	ScoreBest=99999
	IndexSecond=0
	ActualIndex=0
	for a in FULLRAY:
		if a.score < ScoreBest:
			IndexSecond=IndexBest
			IndexBest=ActualIndex
			ScoreBest=a.score
		ActualIndex+=1

	print ActualIndex
	return IndexBest,IndexSecond

def popArray(NEWARRAY,FULLRAY,NEWCOUNT,IndexBest,POPULATION):
	for a in range(0,POPULATION):
		b=random.randint(0,7)
		v1,v2=CrossOver(NEWARRAY[IndexBest].value1,NEWARRAY[IndexBest].value2,FULLRAY[a].value1,FULLRAY[a].value2,b)
		NEWARRAY.append(__CHROMO__(v1,v2))
		NEWARRAY[NEWCOUNT].value1=v1
		NEWARRAY[NEWCOUNT].value2=v2
		NEWARRAY[NEWCOUNT].score=evalu(NEWARRAY[NEWCOUNT].value1,NEWARRAY[NEWCOUNT].value2)
		NEWCOUNT+=1

	return

def CrossOverBest(NEWARRAY,FULLRAY,NEWCOUNT,IndexBest,IndexSecond):
	for a in range(0,7):
		v1,v2=CrossOver(FULLRAY[IndexBest].value1,FULLRAY[IndexBest].value2,FULLRAY[IndexSecond].value1, FULLRAY[IndexSecond].value2,a)
		NEWARRAY.append(__CHROMO__(v1,v2))
		NEWARRAY[NEWCOUNT].value1=v1
		NEWARRAY[NEWCOUNT].value2=v2
		NEWARRAY[NEWCOUNT].score=evalu(NEWARRAY[NEWCOUNT].value1,NEWARRAY[NEWCOUNT].value2)
		NEWCOUNT+=1

	return

def printArray(ARRAY,IndexBest,IndexSecond):
	print IndexBest,ARRAY[IndexBest].value1,ARRAY[IndexBest].value2,ARRAY[IndexBest].score
	print IndexSecond,ARRAY[IndexSecond].value1,ARRAY[IndexSecond].value2,ARRAY[IndexSecond].score
	return

InitArray(FULLRAY,POPULATION)
IndexBest,IndexSecond=findBest(FULLRAY)

printArray(FULLRAY,IndexBest,IndexSecond)

NEWCOUNT=0
NEWARRAY=FULLRAY

for n in range(1,GENERATIONS):
	popArray(NEWARRAY,FULLRAY,NEWCOUNT,IndexBest,POPULATION)
	CrossOverBest(NEWARRAY,FULLRAY,NEWCOUNT,IndexBest,IndexSecond)
	IndexBest,IndexSecond=findBest(NEWARRAY)
	print "Generation: "+str(n)+'\n'
	printArray(NEWARRAY,IndexBest,IndexSecond)
	FULLRAY=NEWARRAY
