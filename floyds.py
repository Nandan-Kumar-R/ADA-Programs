import random
import numpy as np
inf=9999
def floydWarshall(graph,V): 
  
    dist =[i[:] for i in graph] 
    for k in range(V): 
        for i in range(V): 
            for j in range(V): 
                dist[i][j] = min(dist[i][j],(dist[i][k]+dist[k][j]))                                
    print ("The all pair shortest matrix is")
    for i in range(V):
        for j in range(V):
            if(dist[i][j]==9999):
                dist[i][j]=0
    print(np.matrix(dist))
  

m=random.randint(3,4)
graph = [[0 for column in range(m)]for row in range(m)] 
for column in range(m): 
    for row in range(m):
        if(column==row):
            graph[column][row]=0
        else:
            graph[column][row]=(random.randint(1,15) or inf)
            if(graph[column][row]!=inf):
                graph[row][column]=inf
            else:
                graph[row][column]=random.randint(1,15)
                
print("The given graph is ")
print(np.matrix(graph))
 
floydWarshall(graph,m);