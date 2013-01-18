from lib import sorting


#OFILE=open("/home/rob/hits.list","r")
OFILE=open("rand.list","r")
UNSORTLIST=[]
for line in OFILE:
#	line=line.strip().split(' # ')
#	TUP=(line[0],line[1],line[2])
#	UNSORTLIST+=TUP
	UNSORTLIST.append(line)
OFILE.close()

SORTLIST=sorting.QuickSort(UNSORTLIST,0)

#OUTPUT=open("/home/rob/hits.sorted","r")
OUTPUT=open("rand.sorted","r")
for line in SORTLIST:
	OUTPUT.write(line)
	OUTPUT.write('\n')

OUTPUT.close()

