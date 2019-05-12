import random
import numpy as np
class Graph: 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        for column in range(vertices): 
            for row in range(vertices):
                if(column==row):
                    self.graph[column][row]=1
                else:
                    self.graph[column][row]=random.randint(0,1)
                    if(self.graph[column][row]==1):
                        self.graph[row][column]=0
        print(np.matrix(self.graph))


    def printSolution(self, reach): 
        print ("The transitive closure of the given graph is ")	 
        print(np.matrix(reach))
	
	
    def transitiveClosure(self,graph): 
        reach =[i[:] for i in graph] 
        for k in range(self.V): 
            for i in range(self.V): 
                for j in range(self.V): 
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j]) 
        self.printSolution(reach) 


m=random.randint(3,9)
g= Graph(m) 
g.transitiveClosure(g.graph) 

