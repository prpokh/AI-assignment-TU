from common_data import graph, start_node, goal_node, show_student_info

def dls(graph, node, goal, limit, path):
    path.append(node)
    if node == goal:
        return True
    if limit <= 0:
        path.pop()
        return False
        
    for neighbor, _ in graph.get(node, []):
        if neighbor not in path:
            if dls(graph, neighbor, goal, limit - 1, path):
                return True
                
    path.pop()
    return False

limit = 4
path = []
found = dls(graph, start_node, goal_node, limit, path)

print(f"Goal {goal_node} reached within limit {limit}: {path if found else 'Not Found'}")
show_student_info("4 - DLS")