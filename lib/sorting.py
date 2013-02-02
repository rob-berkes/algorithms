import random
from multiprocessing import Process,Manager,Pipe
import pdb
def QuickSort(A):
        if len(A)==1:
                return A
        elif len(A)==0:
                return A
        else:
                PartIndex=random.randint(0,len(A)-1)
                PartitionValue=A.pop(PartIndex)
                lesser=[]
                greater=[]
                for val in range(0,len(A)):
                        if A[val] <= PartitionValue:
                                lesser.append(A[val])
                        else:
                                greater.append(A[val])
                pv=[]
                pv.append(PartitionValue)
        return QuickSort(lesser)+pv+QuickSort(greater)

def QuickSortMP(A,conn,NumProcs):
#	pdb.set_trace()
        if len(A)<=1 :
		conn.send(A)
		conn.close()
	elif int(NumProcs)<1:
		conn.send(QuickSort(A))
		conn.close()
        else:
                PartIndex=random.randint(0,len(A)-1)
                PartitionValue=A.pop(PartIndex)
                lesser=[x for x in A if x < PartitionValue]
                greater=[x for x in A if x >= PartitionValue]
		Procs=int(NumProcs)-1

		pConnLeft,cConnLeft=Pipe()
		leftProc=Process(target=QuickSortMP,args=(lesser,cConnLeft,Procs))
		pConnRight,cConnRight=Pipe()
		rightProc=Process(target=QuickSortMP,args=(greater,cConnRight,Procs))
		

		leftProc.start()
		rightProc.start()

		leftStr=pConnLeft.recv()
		rightStr=pConnRight.recv()

		conn.send(leftStr+[PartitionValue]+rightStr)
#		conn.send(pConnLeft.recv()+[PartitionValue]+pConnRight.recv())
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
#                PartIndex=random.randint(0,len(A)-1)
#                PartitionValue=A.pop(PartIndex)
#                lesser=()
#                greater=()
#                for val in range(0,len(A)):
#                        if A[val][IndexValue] <= PartitionValue[IndexValue]:
#                                lesser.append(A[val])
#                        else:
#                                greater.append(A[val])
#                pv=[]
#                pv.append(PartitionValue)
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

