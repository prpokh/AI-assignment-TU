import matplotlib.pyplot as plt
import networkx as nx
from common_data import game_tree, leaf_values

# Initialize directed graph
G = nx.DiGraph()

# Build tree edges
for parent, children in game_tree.items():
    for child in children:
        G.add_edge(parent, child)

# Explicit layout coordinates (x, y) by depth levels
pos = {
    # Depth 0: MAX (Root)
    'ROOT': (4.5, 3.0),
    
    # Depth 1: MIN
    'MIN_1': (2.25, 2.0),
    'MIN_2': (6.75, 2.0),
    
    # Depth 2: MAX
    'MAX_1': (1.125, 1.0),
    'MAX_2': (3.375, 1.0),
    'MAX_3': (5.625, 1.0),
    'MAX_4': (7.875, 1.0),
    
    # Depth 3: Terminal Leaves
    'L1': (0.5, 0.0), 'L2': (1.75, 0.0),
    'L3': (2.75, 0.0), 'L4': (4.0, 0.0),
    'L5': (5.0, 0.0), 'L6': (6.25, 0.0),
    'L7': (7.25, 0.0), 'L8': (8.5, 0.0)
}

plt.figure(figsize=(11, 7))
plt.title("Game Tree: Minimax with Alpha-Beta Pruning", fontsize=14, fontweight="bold", pad=20)

# Draw tree edges
nx.draw_networkx_edges(G, pos, edge_color="#555555", width=1.5, arrowsize=14)

# Color nodes according to type
internal_nodes = [node for node in G.nodes() if node not in leaf_values]
leaves = list(leaf_values.keys())

# Draw internal decision nodes (circles)
nx.draw_networkx_nodes(
    G, pos,
    nodelist=internal_nodes,
    node_size=1500,
    node_color="#e3f2fd",
    edgecolors="#0d47a1",
    linewidths=2.0
)
nx.draw_networkx_labels(G, pos, labels={n: n for n in internal_nodes}, font_size=8, font_weight="bold")

# Draw leaf nodes (boxes/squares)
nx.draw_networkx_nodes(
    G, pos,
    nodelist=leaves,
    node_size=1100,
    node_color="#fff3e0",
    node_shape="s",
    edgecolors="#e65100",
    linewidths=2.0
)

# Display leaf evaluation values inside leaf boxes
leaf_labels = {k: f"{v}" for k, v in leaf_values.items()}
nx.draw_networkx_labels(G, pos, labels=leaf_labels, font_size=10, font_weight="bold")

# Annotate levels on the left
plt.text(-0.5, 3.0, "MAX (Root)", fontsize=11, fontweight="bold", color="#0d47a1")
plt.text(-0.5, 2.0, "MIN", fontsize=11, fontweight="bold", color="#d32f2f")
plt.text(-0.5, 1.0, "MAX", fontsize=11, fontweight="bold", color="#0d47a1")
plt.text(-0.5, 0.0, "Leaves", fontsize=11, fontweight="bold", color="#e65100")

plt.axis("off")
plt.tight_layout()
plt.savefig("alpha_beta_tree.png", dpi=300)
print("Alpha-Beta Game Tree saved as 'alpha_beta_tree.png'")
plt.show()