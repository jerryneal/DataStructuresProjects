

'''
    Author : Neal, Heui and Niyi
    Date   : 06/17/2015
    Description : Option B involving the Merge, Quick and Heap sort for February CS 320.
'''

import random
from time import time

class time_eff:
       def __init__(self):
             self.A = []
       
       #This function heapifies the process.
       def pushdown(self,A,k,n):
             v = A[k]
             heap = False
             while not heap and 2 * k <= n:
             	 j = 2 * k
             	 if j < n: 
             	 	 if A[j] < A[j+1]:
             	 	 	 j+=1
             	 	 elif v >= A[j]:
             	 	 	 heap = True
             	 	 else:
             	 	 	 A[k] = A[j]
             	 	 	 k = j
             A[k] = v
#-------------------------------------------------------------------------             
       #The heap sort function              
       def heapsort(self,A):	 
             #Stage 1
             #Constructs elements bottom-up
             start_time = time()
             A = [None]+A
             n = len(A)-1
             for i in range(n//2,1):
                     k = i
                     self.pushdown(k,n)
           
             #Stage 2
             #Maximum delete	 
             for i in range(n):
                     A[1],A[n] = A[n],A[1]
                     n-=1
                     self.pushdown(A,1,n)
             return A 
#--------------------------------------------------------------------------            
       #Quick sort algorithm 
       def quicksort(self, A):
       		 l = A[0]
       		 r = A[-1]  
       		 if l<r:
       		 	 #s = self.lumoto_partition(A,l,r)
       		 	 s = 2
       		 	 self.quicksort(A[l:s-1])
       		 	 self.quicksort(A[s+1:l])
       		 	 print("i") 	
       		 return A + A[l:] + A[r:] 
       		 	
       #Lumoto_partition      
       def lumoto_partition(self,A,l,r):
             p = A[l]
             print(p)
             s = l
             for i in range(l+1,r):
             	 if A[i] < p:
             	 	 s += 1
             	 	 A[s],A[i] = A[i],A[s]
             A[l],A[s] = A[s],A[l]
             return s 
#---------------------------------------------------------------------------             
       #Merge sort algorithm
       def mergesort(self,A):
             n = len(A)      
             if n <= 1:
             	 return A
             else:
             	 b = self.mergesort(A[:n//2])
             	 c = self.mergesort(A[n//2:])
             	 A = self.merge(b,c)	  
             return A
             
       #The merge function the two lists
       def merge(self,x,y):
             final_list = []
             n,m = len(x),len(y)
             i,j = 0,0
             while i<n and j<m:
             	 if x[i] < y[i]:
             	 	 final_list.append(x[i])
             	 	 i+=1
             	 else:
             	 	 final_list.append(y[j])
             	 	 j+=1
             return final_list + x[i:] + y[j:]
#---------------------------------------------------------------------------
             	 
def main():
	 num = eval(input("Enter your desired size of n:" ))
	 randomlist = []
	 for i in range(num):
	 	 x = random.randint(0,100)
	 	 randomlist.append(x) 
	 
	 newtime_eff = time_eff()
	 newtime_eff.quicksort(randomlist)
	 
	 sort_type = [newtime_eff.mergesort(randomlist),newtime_eff.quicksort(randomlist),newtime_eff.heapsort(randomlist)]
	 for i in sort_type:
	 	 a = time()
	 	 element[i]
	 	 b = time()
	 	 print("The result of sorting using" +i+ "is" + b - a)	 	 
	 
if __name__ == '__main__':
	main()
