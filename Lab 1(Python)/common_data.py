# Student metadata dictionary
STUDENT_INFO = {
    "Name": "Prasanna Pokharel",
    "Roll No": "24",
    "Lab Number": "Lab I"
}

def show_student_info(extra_label=""):
    print("\n" + "=" * 36)
    for key, val in STUDENT_INFO.items():
        print(f"{key:<12}: {val}")
    if extra_label:
        print(f"Task        : {extra_label}")
    print("=" * 36)

# Graph representation: node -> list of (neighbor, weight)
graph = {
    'S': [('A', 4), ('B', 3)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1), ('E', 6)],
    'C': [('F', 3)],
    'D': [('F', 2), ('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

# Heuristic values h(n) estimating distance to Goal 'G'
heuristics = {
    'S': 11,
    'A': 8,
    'B': 7,
    'C': 6,
    'D': 4,
    'E': 5,
    'F': 3,
    'G': 0
}

start_node = 'S'
goal_node = 'G'

# --- Game Tree Data for Minimax & Alpha-Beta (Question 7) ---
# Adjacency representing tree hierarchy from Root down to leaves
game_tree = {
    'ROOT': ['MIN_1', 'MIN_2'],
    'MIN_1': ['MAX_1', 'MAX_2'],
    'MIN_2': ['MAX_3', 'MAX_4'],
    'MAX_1': ['L1', 'L2'],
    'MAX_2': ['L3', 'L4'],
    'MAX_3': ['L5', 'L6'],
    'MAX_4': ['L7', 'L8']
}

# Terminal evaluation values for leaves L1 through L8
leaf_values = {
    'L1': 3, 'L2': 5,
    'L3': 6, 'L4': 9,
    'L5': 1, 'L6': 2,
    'L7': 0, 'L8': -1
}