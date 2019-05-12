from collections import defaultdict
import random


def dfs(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return path

if __name__ == "__main__" :
    adjacency_matrix = defaultdict(list)
    m=random.randint(2,10)
    b=[]
    b=[[random.randint(0,1) for i in range(m)]for j in range(m)] 
    for i in range(0,m):
        for j in range(0,m):    
            if(i==j):
                b[i][j]=0
            else:
                
                b[i][j]=b[j][i]
    for i in range(0,m):
        for j in range(0,m):
            if(b[i][j]==1):
                adjacency_matrix[i+1].append(j+1)

 
    print(dfs(adjacency_matrix, 1))
   