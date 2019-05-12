
import matplotlib.pyplot as plt
import random
import time


def selsort(val):
    n=len(val)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if val[min] > val[j]:
                val[i] , val[min] = val[min] , val[i]




def mergesort(val):
    if len(val)>1:
        mid=len(val)//2
        l=val[:mid]
        r=val[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                val[k]=l[i]
                i+=1
            else:
                val[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            val[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            val[k]=r[j]
            j+=1
            k+=1


def partition(val,low,high):
    i=(low-1)
    pivot=val[high]
    for j in range(low,high):
        if val[j]<=pivot:
            i=i+1
            val[i],val[j]=val[j],val[i]
    val[i+1],val[high]=val[high],val[i+1]
    return (i+1)
def quicksort(val,low,high):
    if low<high:
        pi=partition(val,low,high)
        quicksort(val,low,pi-1)
        quicksort(val,pi+1,high)


def inssort(val):
    for i in range(1,len(val)):
        key=val[i]
        j=i-1
        while j>=0 and key<val[j]:
            val[j+1]=val[j]
            j-=1
        val[j+1]=key


def heapify(val,n,i):
    largest=i
    L=2*i+1
    R=2*i+1
    if L<n and val[i]<val[L]:
        largest=L
    if R<n and val[largest] < val[R]:
        largest=R
    if largest !=i:
        val[i],val[largest]=val[largest],val[i]
        heapify(val,n,largest)
def heasort(val):
    n=len(val)
    for i in range(n,-1,-1):
        heapify(val,n,i)
    for i in range(n-1,0,-1):
        val[i],val[0]=val[0],val[i]
        heapify(val,i,0)
        
        
timems=[]
timess=[]
timeqs=[]
timeis=[]
timehs=[]
n_value=[]
for j in range(30):
    val=[]
    n_value.append(60*j)
    for i in range(n_value[j]):
        val.append(random.randint(1,60*j))
    start=time.time()
    selsort(val)
    end=time.time()
    timess.append(end-start)
    start=time.time()
    mergesort(val)
    end=time.time()
    timems.append(end-start)
    start=time.time()
    quicksort(val,0,len(val)-1)
    end=time.time()
    timeqs.append(end-start)
    start=time.time()
    inssort(val)
    end=time.time()
    timeis.append(end-start)
    start=time.time()
    heasort(val)
    end=time.time()
    timehs.append(end-start)
   
plt.plot(n_value,timess,label="Selection")

plt.plot(n_value,timems,label="Merge")
plt.plot(n_value,timeqs,label="Quick")
plt.plot(n_value,timeis,label="Insertion")
plt.plot(n_value,timehs,label="Heap")
plt.legend()
plt.show()


