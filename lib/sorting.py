import random
from multiprocessing import Process,Manager,Pipe
def QuickSort(A):
        if len(A)==1:
                return A
        elif len(A)==0:
                return A
        else:
                PivotIndex=random.randint(0,len(A)-1)
                PivotValue=int(A.pop(PivotIndex))
                lesser=[]
                greater=[]
                pv=[]
                pv.append(PivotValue)
                for val in range(0,len(A)):
                        if int(A[val]) <= PivotValue:
                                lesser.append(int(A[val]))
			elif int(A[val]) == PivotValue:
				pv.append(int(A[val]))
                        else:
                                greater.append(int(A[val]))
        return QuickSort(lesser)+pv+QuickSort(greater)
def QuickSortListArray(A):
        if len(A)==1:
                return A
        elif len(A)==0:
                return A
        else:
                PivotIndex=random.randint(0,len(A)-1)
                PivotValue=A.pop(PivotIndex)
                lesser=[]
                greater=[]
                pv=[]
                pv.append(PivotValue)
                for val in A:
                        if int(val[0]) <= PivotValue[0]:
                                lesser.append(val)
			elif int(val[0]) == PivotValue[0]:
				pv.append(val)
                        else:
                                greater.append(val)
        return QuickSortListArray(lesser)+pv+QuickSortListArray(greater)

def QuickSortMP(A,conn,NumProcs):
        if len(A)<=1 :
		conn.send(A)
		conn.close()
	elif int(NumProcs)<1:
		conn.send(QuickSort(A))
		conn.close()
        else:
                PivotIndex=random.randint(0,len(A)-1)
                PivotValue=A.pop(PivotIndex)
		pv=[]
		pv.append(int(PivotValue))
                lesser=[int(x) for x in A if x < PivotValue]
                greater=[int(x) for x in A if x >= PivotValue]
		Procs=int(NumProcs)-1
		
		pConnLeft,cConnLeft=Pipe()
		leftProc=Process(target=QuickSortMP,args=(lesser,cConnLeft,Procs))
		pConnRight,cConnRight=Pipe()
		rightProc=Process(target=QuickSortMP,args=(greater,cConnRight,Procs))
		

		leftProc.start()
		rightProc.start()

		leftStr=pConnLeft.recv()
		rightStr=pConnRight.recv()
		conn.send(leftStr+pv+rightStr)
#		conn.send(pConnLeft.recv()+[PivotValue]+pConnRight.recv())
		conn.close()
	
		leftProc.join()
		rightProc.join()
        return
def QuickSortMPListArray(A,conn,NumProcs):
	print 'starting mplarray'
        if len(A)<=1 :
		conn.send(A)
		conn.close()
	elif int(NumProcs)<1:
		conn.send(QuickSortListArray(A))
		conn.close()
        else:
                PivotIndex=random.randint(0,len(A)-1)
                PivotValue=A.pop(PivotIndex)
		pv=[]
		pv.append(PivotValue)
                lesser=[x for x in A if x[0] < PivotValue]
                greater=[x for x in A if x[0] >= PivotValue]
		Procs=int(NumProcs)-1
		
		pConnLeft,cConnLeft=Pipe()
		leftProc=Process(target=QuickSortMPListArray,args=(lesser,cConnLeft,Procs))
		pConnRight,cConnRight=Pipe()
		rightProc=Process(target=QuickSortMPListArray,args=(greater,cConnRight,Procs))
		

		leftProc.start()
		rightProc.start()

		leftStr=pConnLeft.recv()
		rightStr=pConnRight.recv()
		conn.send(leftStr+pv+rightStr)
#		conn.send(pConnLeft.recv()+[PivotValue]+pConnRight.recv())
		conn.close()
	
		leftProc.join()
		rightProc.join()
        return
def QuickSortStub(A,conn,NumProcs):

	return
#def QuickSort(A,IndexValue):
#        if len(A)==1:
#                return A
#        elif len(A)==0:
#                return A
#        else:
#                PivotIndex=random.randint(0,len(A)-1)
#                PivotValue=A.pop(PivotIndex)
#                lesser=()
#                greater=()
#                for val in range(0,len(A)):
#                        if A[val][IndexValue] <= PivotValue[IndexValue]:
#                                lesser.append(A[val])
#                        else:
#                                greater.append(A[val])
#                pv=[]
#                pv.append(PivotValue)
#        return QuickSort(lesser)+pv+QuickSort(greater)
def BubbleSort(A):
        swap_done=True
        while swap_done:
                swap_done=False
                for valu in range(0,len(A)-1):
                        if A[valu] > A[valu+1]:
                                swap_done=True
                                t=A[valu+1]
                                A[valu+1]=A[valu]
                                A[valu]=t

        return A

