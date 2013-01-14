import random

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

