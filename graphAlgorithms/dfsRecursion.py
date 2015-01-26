

def dfsRecursive(graph, start, visited=[]):
	visited.extend([start])
	for x in graph[start]:
		if x not in visited:
			path = dfsRecursive(graph, x, visited)
	return visited		
	

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print dfsRecursive(graph, 'A', visited=[])							