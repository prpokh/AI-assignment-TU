from collections import deque

def water_jug_bfs(cap_a=4, cap_b=3, target=2):
    # State: (jug_a, jug_b)
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = set([initial_state])

    while queue:
        (a, b), path = queue.popleft()

        # Goal condition: exactly target gallons in jug A
        if a == target:
            return path + [(a, b)]

        # Generate all 6 possible production rules
        possible_moves = [
            ((cap_a, b), f"Fill 4-gallon jug: ({cap_a}, {b})"),
            ((a, cap_b), f"Fill 3-gallon jug: ({a}, {cap_b})"),
            ((0, b), f"Empty 4-gallon jug: (0, {b})"),
            ((a, 0), f"Empty 3-gallon jug: ({a}, 0)"),
            # Pour A -> B
            ((max(0, a - (cap_b - b)), min(cap_b, b + a)), 
             f"Pour from 4-gal to 3-gal: ({max(0, a - (cap_b - b))}, {min(cap_b, b + a)})"),
            # Pour B -> A
            ((min(cap_a, a + b), max(0, b - (cap_a - a))), 
             f"Pour from 3-gal to 4-gal: ({min(cap_a, a + b)}, {max(0, b - (cap_a - a))})")
        ]

        for next_state, action in possible_moves:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(a, b, action)]))

    return None

solution = water_jug_bfs()
print("--- Water Jug Solution Steps ---")
for step, (a, b, action) in enumerate(solution[:-1], 1):
    print(f"Step {step}: {action}")
print(f"Goal Reached: State is {solution[-1]}\n")

print("Name: Prasanna Pokharel")
print("Rollno: 24") 
print("LAB IV-3")