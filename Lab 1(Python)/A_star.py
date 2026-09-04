import heapq
from common_data import graph, heuristics, start_node, goal_node, show_student_info

def a_star(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    g_cost = {start: 0}
    
    while pq:
        f, g, node, path = heapq.heappop(pq)
        
        if node == goal:
            return g, path
            
        for neighbor, weight in graph.get(node, []):
            tentative_g = g + weight
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + h.get(neighbor, 0)
                heapq.heappush(pq, (f_cost, tentative_g, neighbor, path + [neighbor]))
    return float('inf'), []

cost, path = a_star(graph, heuristics, start_node, goal_node)
print(f"A* Path: {path} with Cost: {cost}")
show_student_info()