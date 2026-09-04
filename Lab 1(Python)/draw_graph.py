import matplotlib.pyplot as plt
import networkx as nx

# 1. Initialize an undirected graph
G = nx.Graph()

# 2. Add edges with weights
edges = [
    ('A', 'B', 4), ('A', 'F', 2),
    ('B', 'C', 3), ('B', 'D', 2),
    ('C', 'D', 1), ('C', 'E', 5),
    ('D', 'E', 7),
    ('F', 'G', 1), ('F', 'H', 3),
    ('G', 'I', 1),
    ('H', 'I', 2),
    ('E', 'I', 2), ('E', 'J', 3),
    ('I', 'J', 5)
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# 3. Node Heuristics h(n)
heuristics = {
    'A': 10, 'B': 3, 'C': 2, 'D': 2, 'E': 3,
    'F': 5,  'G': 4, 'H': 3, 'I': 0, 'J': 0
}

# 4. Manual coordinates matching the diagram layout
pos = {
    'A': (5, 9),
    'B': (3, 6.5),
    'F': (7.5, 7.5),
    'D': (4.8, 5.8),
    'G': (6.3, 6.7),
    'H': (8.5, 5.8),
    'C': (2.8, 4.3),
    'I': (7.2, 5.0),
    'E': (4.8, 2.7),
    'J': (6.3, 2.0)
}

# 5. Plot setup
plt.figure(figsize=(8, 9))
plt.title("LAB-I: Search Graph", fontsize=14, fontweight="bold")

# Draw Nodes
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color='white', edgecolors='black', linewidths=1.8)

# Draw Node Names (inside circles)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_weight='bold')

# Draw Edges
nx.draw_networkx_edges(G, pos, width=1.5, edge_color='black')

# Draw Edge Costs (weights)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=11, font_color='black')

# Draw Heuristic values next to each node (offset slightly to the top-left)
offset_pos = {
    k: (v[0] - 0.25, v[1] + 0.35) for k, v in pos.items()
}
# Adjust 'A' to be directly above
offset_pos['A'] = (pos['A'][0], pos['A'][1] + 0.4)

for node, (x, y) in offset_pos.items():
    plt.text(x, y, str(heuristics[node]), fontsize=11, fontweight='bold', color='black', ha='center')

# Adjust layout and save high-resolution image for A4 printing
plt.axis('off')
plt.tight_layout()
plt.savefig("lab1_graph.png", dpi=300)
plt.show()