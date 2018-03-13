import numpy as np
import datetime

class Array_creation: 
    def __init__(self,n):
        self.A = np.round(np.random.randn(n)*100)

class Sorting:
    def Insertion_sort (self,A,n):
        if n > 0:
            self.Insertion_sort(A,n-1)    
            x = A[n]    
            j = n-1    
            while j>=0 and A[j]>x:
                A[j+1] = A[j]    
                j-=1    
            A[j+1] = x    
        return A
    
    def Quick_sort(self,A):
        pass

    def Heapsort(self,A,n):    
        pass
 
    def Creat_Max_Heap(self,A):
        for start in range(int(np.floor((np.shape(A)[0])/2)),-1,-1):
            A = self.sift_down(A,start,np.shape(A)[0]-1)
        return A

    def Heap_Sorting(self,A,end):
        A = self.Creat_Max_Heap(A)
        for end in range(int(np.shape(A)[0]-1),0,-1):
            A[0], A[end] = A[end],A[0]
            A = self.sift_down(A,0,end-1)
        return A

    def sift_down(self,A,start,end):
        root=start
        while True:
            child = 2*root+1
            if child > end:
                break
            if child+1 <= end and A[child]<A[child+1]:
                child += 1
            if A[root]<A[child]:
                A[root],A[child] = A[child],A[root]
                root = child
            else:
                break
        return A

if __name__=='__main__':
    size = 1000
    A = Array_creation(size)
    array_A = A.A
    array_B = A.A
    sorting = Sorting()
    time0 = datetime.datetime.now()
    array_insertion = sorting.Insertion_sort(array_A,size-1)
    time1 = datetime.datetime.now()
    computation_time_of_insertion = (time1-time0).total_seconds()
    time0 = datetime.datetime.now()
    array_heapSorting = sorting.Heap_Sorting(array_B,size)
    time1 = datetime.datetime.now()
    computation_time_of_heapSorting = (time1-time0).total_seconds()
    print('Result of insertion sorting: {0} \n time cost: {2} \n Result of heap sorting: {1}\n time cost{3}'.format(array_A,array_B,computation_time_of_insertion,computation_time_of_heapSorting))