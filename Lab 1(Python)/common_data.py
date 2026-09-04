# common_data.py

# Student metadata dictionary
STUDENT_INFO = {
    "Name": "Your Full Name",
    "Roll No": "Your Roll Number",
    "Lab Number": "Lab I"
}

def show_student_info(extra_label=""):
    print("\n" + "=" * 35)
    for key, val in STUDENT_INFO.items():
        print(f"{key:<12}: {val}")
    if extra_label:
        print(f"Task        : {extra_label}")
    print("=" * 35)

# Shared graph from image
graph = {
    'A': [('B', 4), ('F', 2)],
    'B': [('A', 4), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 7)],
    'E': [('C', 5), ('D', 7), ('I', 2), ('J', 3)],
    'F': [('A', 2), ('G', 1), ('H', 3)],
    'G': [('F', 1), ('I', 1)],
    'H': [('F', 3), ('I', 2)],
    'I': [('G', 1), ('H', 2), ('E', 2), ('J', 5)],
    'J': [('E', 3), ('I', 5)]
}

# Shared heuristic values
heuristics = {
    'A': 10, 'B': 3, 'C': 2, 'D': 2, 'E': 3,
    'F': 5,  'G': 4, 'H': 3, 'I': 0, 'J': 0
}

start_node = 'A'
goal_node = 'J'