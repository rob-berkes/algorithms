from lib import sorting


#OFILE=open("/home/rob/hits.list","r")
OFILE=open("rand.list","r")
UNSORTLIST=[]
for line in OFILE:
	line=line.strip()
	UNSORTLIST.append(line)
OFILE.close()

SORTLIST=sorting.QuickSortMP(UNSORTLIST)

#OUTPUT=open("/home/rob/hits.sorted","w")
OUTPUT=open("rand.sorted","w")
for line in SORTLIST:
	OUTPUT.write(line)
	OUTPUT.write('\n')

OUTPUT.close()

