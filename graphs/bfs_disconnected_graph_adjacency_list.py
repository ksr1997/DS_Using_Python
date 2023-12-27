import queue 

def addEdge(adj, u, v): 
	adj[u].append(v) 

def BFSUtil(u, adj, visited): 
	
	q = queue.Queue() 
	visited[u] = True
	q.put(u) 
	
	while(not q.empty()): 
		u = q.queue[0] 
		print(u, end = " ") 
		q.get() 
		i = 0
		while i != len(adj[u]): 
			if (not visited[adj[u][i]]): 
					visited[adj[u][i]] = True
					q.put(adj[u][i]) 
			i += 1

def BFS(adj, V): 
	visited = [False] * V 
	for u in range(V): 
		if (visited[u] == False): 
			BFSUtil(u, adj, visited) 

# Driver code 
if __name__ == '__main__': 

	V = 5
	adj = [[] for i in range(V)] 

	addEdge(adj, 0, 4) 
	addEdge(adj, 1, 2) 
	addEdge(adj, 1, 3) 
	addEdge(adj, 1, 4) 
	addEdge(adj, 2, 3) 
	addEdge(adj, 3, 4) 
	print(adj)
	BFS(adj, V) 
