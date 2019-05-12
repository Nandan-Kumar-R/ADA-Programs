import random
from collections import defaultdict

def bfs(graph, start):
    explored = []
    queue = [start]
    levels = {}      
    levels[start]= 0    
    visited= [start]     
    while queue:
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                levels[neighbour]= levels[node]+1
    return explored

if __name__ == "__main__" :
    adjacency_matrix= defaultdict(list)
    m=random.randint(2,10)
    b=[]; columns=[]
    for i in range(0,m):
        b+= [0]
    for j in range (0,m):
        columns += [0]
    for i in range (0,m):
        b[i] = columns
    for i in range(0,m):
        for j in range(0,m):    
            b[i][j]=random.randint(0,1)
    for i in range(0,m):
        for j in range(0,m):
            if(b[i][j]==1):
                adjacency_matrix[i+1].append(j+1)   
    print(bfs(adjacency_matrix, 1))
   