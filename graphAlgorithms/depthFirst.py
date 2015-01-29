# Iterative

def dfsIterative(graph, start):
	stack, visited = [], set()
	stack.append(start)
	while(stack):
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited		

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print dfsIterative(graph, 'A')			
