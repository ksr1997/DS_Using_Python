import queue 

def add_edge(edges, f, s): 
	edges[f][s] = 1

def print_bfs(edges, V, start, visited): 
	if V == 0: 
		return
	bfs = queue.Queue() 
	bfs.put(start) 
	visited[start] = 1
	while not bfs.empty(): 
		data = bfs.get() 
		print(data, end=' ') 
		for i in range(V): 
			if edges[data][i] == 1: 
				if visited[i] == 0: 
					bfs.put(i) 
					visited[i] = 1

def bfs_helper(edges, V): 
	if V == 0: 
		return
	visited = [0] * V 
	for i in range(V): 
		if visited[i] == 0: 
			print_bfs(edges, V, i, visited) 

if __name__ == "__main__": 
	V = 5
	E = 6
	if E == 0: 
		for i in range(V): 
			print(i, end=' ') 
		exit() 

	edges = [[0 for _ in range(V)] for _ in range(V)] 

	add_edge(edges, 0, 4) 
	add_edge(edges, 1, 2) 
	add_edge(edges, 1, 3) 
	add_edge(edges, 1, 4) 
	add_edge(edges, 2, 3) 
	add_edge(edges, 3, 4) 

	bfs_helper(edges, V) 
