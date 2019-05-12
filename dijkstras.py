import sys
import random
class Graph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	def printSolution(self, dist): 
		print ("Vertex Distance from Source")
		for node in range(self.V): 
			print ("Node %d--->%d"%(node,dist[node]))

	def minDistance(self, dist, sptSet): 
		min = sys.maxsize 
		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 
		return min_index 

	def dijkstra(self, src): 
		dist = [sys.maxsize] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 
		for cout in range(self.V):  
			u = self.minDistance(dist, sptSet) 
			sptSet[u] = True
			for v in range(self.V): 
				if (self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]): 
						dist[v] = dist[u] + self.graph[u][v] 
		self.printSolution(dist) 


m=random.randint(3,4)
g = Graph(m) 
for column in range(m): 
    for row in range(m):
        if(column==row):
            g.graph[column][row]=0
        else:
            g.graph[column][row]=random.randint(0,15)
            g.graph[row][column]=g.graph[column][row]
print(g.graph)
g.dijkstra(0); 
