import random 
import time
from time import clock
import matplotlib.pyplot as plt

a=[]
nValues=[]
binaryTime=[]
linearTime=[]
interpolationTime=[]

def binarySearch(a,key):
	first=0
	last=len(a)-1
	found=0

	while first<=last and not found:
		mid=(first+last)//2
		if a[mid]==key:
			found=1
		else:
			if(a[mid]>key):
				last=mid-1
			else:
				first=mid+1
	return found


def linearSearch(a,n,key):
	for i in range(n):
		if a[i]==key:
			return i
	return -1

def interpolationSearch(a,key):
	n=len(a)
	low=0
	high=n-1

	while low<=high and key>=a[low] and key<=a[high]:
		if low==high:
			if a[low]==key:
				return low
			return -1

		pos=low+int(((float(high-low)/(a[high]-a[low]))*(key-a[low])))

		if a[pos]==key:
			return pos

		else:
			high=pos-1

	return -1



for i in range(10):
	n=i*200
	a=[]
	nValues.append(n)
	for j in range(n):
		temp=random.randint(0,100)
		a.append(temp)
	key=random.randint(0,100)

	start=time.perf_counter()
	linearSearch(a,n,key)
	end=time.perf_counter()
	diff=end-start
	linearTime.append(diff)

	a.sort()

	start=time.perf_counter()
	binarySearch(a,key)
	end=time.perf_counter()
	diff=end-start
	binaryTime.append(diff)

	start=time.perf_counter()
	interpolationSearch(a,key)
	end=time.perf_counter()
	diff=end-start
	interpolationTime.append(diff)

print(nValues)
print(binaryTime)
print(linearTime)
print(interpolationTime)

plt.plot(nValues,linearTime,label="Linear Search")
plt.plot(nValues,binaryTime,label="Binary Search")
plt.plot(nValues,interpolationTime,label="Interpolation Search")
plt.legend()
plt.show()