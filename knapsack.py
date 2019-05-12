import random

def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif (wt[i-1] <= w): 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w]   
    return K[n][W] 
 
    
n=random.randint(4,9)
val = [0 for i in range(n)] 
wt = [0 for i in range(n)] 
W = random.randint(20,100)
print("The knapsack capacity is %d" % W)
for i in range(n):
    val[i]=random.randint(20,100)
    wt[i]=random.randint(2,W)
print("The value array is,")
print(val)
print("The weight array is,")
print(wt)
print("The maximum profit is,")
print(knapSack(W, wt, val, n)) 