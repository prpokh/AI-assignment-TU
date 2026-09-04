import heapq
from common_data import graph, start_node, goal_node, show_student_info

def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = {}
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        
        if node == goal:
            return cost, path
            
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return float('inf'), []

cost, path = ucs(graph, start_node, goal_node)
print(f"UCS Optimal Path: {path} with Total Cost: {cost}")
show_student_info("3 - UCS")