from common_data import graph, start_node, goal_node, show_student_info

def dfs(graph, node, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
        
    visited.add(node)
    path.append(node)
    
    if node == goal:
        return path
        
    for neighbor, _ in graph.get(node, []):
        if neighbor not in visited:
            res = dfs(graph, neighbor, goal, visited, path)
            if res:
                return res
                
    path.pop()
    return None

path = dfs(graph, start_node, goal_node)
print(f"DFS Path from {start_node} to {goal_node}: {path}")
show_student_info()