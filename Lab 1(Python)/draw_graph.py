import matplotlib.pyplot as plt
import networkx as nx
from common_data import graph, heuristics, start_node, goal_node

# 1. Initialize directed graph
G = nx.DiGraph()

for u, neighbors in graph.items():
    for v, w in neighbors:
        G.add_edge(u, v, weight=w)

# 2. Geometric coordinates matching the diagram layout
pos = {
    'S': (4.0, 8.0),
    'A': (2.0, 6.0),
    'B': (6.0, 6.0),
    'C': (1.0, 4.0),
    'D': (3.5, 4.0),
    'E': (7.0, 4.0),
    'F': (2.5, 1.8),
    'G': (5.5, 1.8)
}

# 3. Canvas setup
plt.figure(figsize=(9, 8))
plt.title("LAB-I: State Space Search Graph", fontsize=15, fontweight="bold", pad=20)

# Draw edges with directional arrows
nx.draw_networkx_edges(
    G, pos,
    arrowstyle="->",
    arrowsize=18,
    edge_color="#333333",
    width=1.8,
    node_size=1600
)

# Highlight Start (green) and Goal (orange)
node_colors = []
for node in G.nodes():
    if node == start_node:
        node_colors.append("#d4edda")  # Soft green
    elif node == goal_node:
        node_colors.append("#ffeeba")  # Soft amber
    else:
        node_colors.append("#ffffff")  # White

# Draw node circles
nx.draw_networkx_nodes(
    G, pos,
    node_size=1500,
    node_color=node_colors,
    edgecolors="black",
    linewidths=2.0
)

# Draw node letter labels inside circles
nx.draw_networkx_labels(G, pos, font_size=13, font_weight="bold")

# Draw edge weights (step costs)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=edge_labels,
    font_size=11,
    font_color="#b30000",
    font_weight="bold"
)

# Render heuristic values h(n) right above each node
for node, (x, y) in pos.items():
    h_text = f"h={heuristics[node]}"
    plt.text(x, y + 0.42, h_text, fontsize=11, fontweight="bold", color="#004085", ha="center")

# Visual legends
plt.text(0.5, 8.5, f"Start Node: {start_node}", fontsize=11, color="green", fontweight="bold")
plt.text(0.5, 8.1, f"Goal Node : {goal_node}", fontsize=11, color="orange", fontweight="bold")

plt.axis("off")
plt.tight_layout()
plt.savefig("lab1_graph.png", dpi=300)
print("Graph saved successfully as 'lab1_graph.png'.")
plt.show()