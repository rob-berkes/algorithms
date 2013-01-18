import random
from multiprocessing import Process,Manager

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

def QuickSortMP(A):
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
		l1=lesser
		g1=greater
		p1=Process(target='QuickSortMP',args=l1)
		p2=Process(target='QuickSortMP',args=g1)
		p1.start()
		p2.start()
		p1.join()
		p2.join()
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

