from collections import deque
from collections import defaultdict

def bfs(graph, start, visited, path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    
    while len(queue) != 0:
        current_node = queue.popleft()
        
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                path.append(neighbor)
    
    return path

graph = defaultdict(list)
v, e = map(int, input().split())  

for _ in range(e):
    u, v = input().split() 
    graph[u].append(v)
    graph[v].append(u)  

start = 'A'  
path = []
visited = defaultdict(bool)

traversed_path = bfs(graph, start, visited, path)
print(traversed_path)
