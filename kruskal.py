import random
from collections import defaultdict     
m=random.randint(3,9)
parent=[0 for n in range(m)]
     
def find(i): 
    while (parent[i] != i):
        i = parent[i] 
    return i 
  
def union1(i, j): 
    a = find(i) 
    b = find(j) 
    parent[a] = b

  
def kruskalMST(graph):
    mincost = 0  
    for i in range(m): 
        parent[i] = i 
    edge_count = 0 
    while (edge_count < m-1):  
        min,a,b=99999,-1,-1
        for i in range(m):
            for j in range(m): 
                if ( find(i) != find(j) and graph[i][j]<min and graph[i][j]!=0): 
                    min = graph[i][j] 
                    a = i 
                    b = j
        union1(a, b) 
        print("Edge %d:(%d, %d) cost:%d "% (edge_count+1, a, b, min))
        edge_count+=1
        mincost += min;     
    print("Minimum cost= ", mincost)
       
        
if __name__ == "__main__" : 
    graph = [[0 for column in range(m)]  
        for row in range(m)] 
    for column in range(m): 
        for row in range(m):
            if(column==row):
                graph[column][row]=99999
            else:
                graph[column][row]=random.randint(1,15)
                graph[row][column]=graph[column][row]
    print(graph)  
    kruskalMST(graph) 