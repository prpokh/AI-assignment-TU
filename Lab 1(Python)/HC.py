from common_data import graph, heuristics, start_node, show_student_info

def hill_climbing(graph, h, start):
    current = start
    path = [current]
    
    while True:
        neighbors = graph.get(current, [])
        if not neighbors:
            break
            
        # Select neighbor with the lowest heuristic value (closest to goal)
        best_neighbor = min(neighbors, key=lambda n: h[n[0]])[0]
        
        # Stop if no strictly better neighbor exists (local optimum reached)
        if h[best_neighbor] >= h[current]:
            break
            
        current = best_neighbor
        path.append(current)
        
    return path, current, h[current]

path, peak, h_val = hill_climbing(graph, heuristics, start_node)
print(f"Hill Climbing Path: {path}")
print(f"Terminated at Node: {peak} with Heuristic: {h_val}")
show_student_info()