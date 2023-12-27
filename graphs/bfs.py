#Breadth First Search
#Uses Queues

'''
logic:
Graph format:
dictionary 
key:vertices,
values:link or edge connection to that particular vertice

two lists:
1:visited with true or false
2:Queue

Add element to queue, visited to true for that particular vertice

while q:
get that element, loop through the values, 
update visited list,add to queue
'''

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,s):
        visited=[False]*(max(self.graph)+1)
        # print(max(self.graph))
        # print(visited)
        queue=[]
        queue.append(s)
        visited[s]=True

        while queue:
            s=queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
if __name__=='__main__':
    g=Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.bfs(2)