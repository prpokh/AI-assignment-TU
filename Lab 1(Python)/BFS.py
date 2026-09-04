from collections import deque
from common_data import graph, start_node, goal_node, show_student_info

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
            
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

path = bfs(graph, start_node, goal_node)
print(f"BFS Path from {start_node} to {goal_node}: {path}")
show_student_info()