import random

# Use Case: Find the optimal 4-bit combination '1111' (Decimal 15)
TARGET_FITNESS = 4

# Fitness function: Count of 1-bits in a 4-bit integer
def fitness(x):
    return bin(x).count('1')

# Initial population: 6 random 4-bit integers (0 to 15)
population = [random.randint(0, 15) for _ in range(6)]

generation = 0

while True:
    print(f"\nGeneration {generation}")
    print("Population:", [f"{x:04b}" for x in population])

    # Rank candidates by fitness
    scores = [(fitness(x), x) for x in population]
    scores.sort(reverse=True)

    parent1 = scores[0][1]
    parent2 = scores[1][1]

    print(f"Parents: {parent1:04b} (Fit: {scores[0][0]}), {parent2:04b} (Fit: {scores[1][0]})")

    # Natural termination: stop as soon as perfect fitness (4) is reached
    if scores[0][0] == TARGET_FITNESS:
        best = parent1
        break

    # Crossover: split 4 bits at midpoint (top 2 bits: 12 / '1100', bottom 2 bits: 3 / '0011')
    child1 = (parent1 & 12) | (parent2 & 3)
    child2 = (parent2 & 12) | (parent1 & 3)

    # Mutation: 30% chance to flip the least significant bit
    if random.random() < 0.3:
        child1 ^= 1
    if random.random() < 0.3:
        child2 ^= 1

    # Next generation: 2 parents + 2 children + 2 new random candidates
    population = [
        parent1,
        parent2,
        child1,
        child2,
        random.randint(0, 15),
        random.randint(0, 15)
    ]

    generation += 1

print("\nOptimal Solution Found!")
print("Best Solution (Binary)  =", f"{best:04b}")
print("Best Solution (Decimal) =", best)
print(f"Fitness                 = {fitness(best)}/{TARGET_FITNESS}")
print("Generations Taken       =", generation)


print("\nPrasanna Pokharel")
print("Rollno: 24")
print("LAB IV-4")