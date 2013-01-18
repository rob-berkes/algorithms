import random
class __CHROMO__:
	value1=random.randint(0,10)+5.0
	value2=random.randint(0,10)-5.0
	score=0


		
POPULATION=2000

FULLRAY=[]
# Equation: 8x^2-10x-3
def evalu(value1,value2):
	score1=((value1*value1)*8)-(value1*10)-3
	score2=((value2*value2)*8)-(value2*10)-3
	summa=score1+score2
	return summa
def InitVars():
	v1=random.random()*10+5.0
	v2=random.random()*10-5.0
	return v1,v2
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
for a in range(0,POPULATION):
#	FULLRAY.append(__CHROMO__())
	t=__CHROMO__()
	t.value1,t.value2=InitVars()
	t.score=0
	FULLRAY.append(t)
	FULLRAY[a].score=evalu(FULLRAY[a].value1,FULLRAY[a].value2)

IndexBest,IndexSecond=findBest(FULLRAY)


print IndexBest,FULLRAY[IndexBest].value1,FULLRAY[IndexBest].value2,FULLRAY[IndexBest].score
print IndexSecond,FULLRAY[IndexSecond].value1,FULLRAY[IndexSecond].value2,FULLRAY[IndexSecond].score

NEWCOUNT=0
for a in range(0,POPULATION):
	for b in range(0,7):
		FULLRAY[NEWCOUNT].value1,FULLRAY[NEWCOUNT].value2=CrossOver(FULLRAY[IndexBest].value1,FULLRAY[IndexBest].value2,FULLRAY[a].value1,FULLRAY[a].value2,b)
		NEWCOUNT+=1

IndexBest,IndexSecond=findBest(FULLRAY)
print IndexBest,FULLRAY[IndexBest].value1,FULLRAY[IndexBest].value2,FULLRAY[IndexBest].score
print IndexSecond,FULLRAY[IndexSecond].value1,FULLRAY[IndexSecond].value2,FULLRAY[IndexSecond].score
