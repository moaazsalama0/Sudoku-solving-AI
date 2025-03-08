import random

# Fitness function
def calculate_fitness(grid):
    total_diff = 0
    
    # Initialize penalties for rows, columns, and subgrids
    row_penalty = 0
    col_penalty = 0
    subgrid_penalty = 0
    
    # Row fitness: Count how many duplicates are in each row
    for row in grid:
        row_penalty += count_duplicates(row)
    
    # Column fitness: Count how many duplicates are in each column
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        col_penalty += count_duplicates(column)
    
    # Subgrid fitness: Count how many duplicates are in each 3x3 subgrid
    for subgrid in extract_subgrids(grid):
        subgrid_penalty += count_duplicates(subgrid)
    
    # Summing penalties for rows, columns, and subgrids
    total_diff += row_penalty + col_penalty + subgrid_penalty
    
    return total_diff

def count_duplicates(values):
    """Returns the number of duplicate values in a list, ignoring zeros (empty cells)."""
    seen = set()
    duplicates = 0
    for value in values:
        if value != 0:  # Ignore empty cells
            if value in seen:
                duplicates += 1
            seen.add(value)
    return duplicates

def extract_subgrids(grid):
    """Extracts the 3x3 subgrids from a 9x9 grid."""
    subgrids = []
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(grid[r + i][c + j])
            subgrids.append(subgrid)
    return subgrids



# Replace zeros with random values
def replace_zeros_with_random(matrix):
    for i in range(9):  # Iterate over rows
        for j in range(9):  # Iterate over columns
            if matrix[i][j] == 0:  # If the cell is zero
                matrix[i][j] = random.randint(1, 9)  # Replace with random number
    return matrix

# Crossover function
def crossover(parent1, parent2):
    child = [row[:] for row in parent1]
    # Randomly swap 3x3 subgrids
    grid_row = random.choice([0, 3, 6])  # Choose a random 3x3 block row
    grid_col = random.choice([0, 3, 6])  # Choose a random 3x3 block column
    for r in range(3):
        for c in range(3):
            child[grid_row + r][grid_col + c] = parent2[grid_row + r][grid_col + c]
    return child


# Mutation function
def mutate(grid, mutation_rate):
    mutated = [row[:] for row in grid]
    if random.random() < mutation_rate:  # Mutation based on dynamic mutation rate
        row, col = random.randint(0, 8), random.randint(0, 8)
        mutated[row][col] = random.randint(1, 9)
    return mutated

# Extract subgrids
def extract_subgrids(grid):
    subgrids = []
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            subgrid = []
            for row in range(3):
                for col in range(3):
                    subgrid.append(grid[box_row + row][box_col + col])
            subgrids.append(subgrid)
    return subgrids

# Print grid
def Printgrid(Grid):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y == 6):
                print("|", end=" ")
            print(" " + str(Grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)

# Initialize population
def initialize_population(size=100):
    return [replace_zeros_with_random([[0] * 9 for _ in range(9)]) for _ in range(size)]

# Main function
def genetic_algorithm():
    population = initialize_population(size=100)
    generations = 500
    best_fitness = float('inf')
    stagnation_count = 0
    mutation_rate = 0.2  # Initial mutation rate
    
    for gen in range(generations):
        # Calculate fitness for each individual
        fitness_scores = [(calculate_fitness(ind), ind) for ind in population]
        fitness_scores.sort(key=lambda x: x[0])  # Sort by fitness (lower is better)
        
        # Output the best fitness in this generation
        print(f"Generation {gen + 1}: Best Fitness = {fitness_scores[0][0]}")
        
        # If best fitness is 0, solution found
        if fitness_scores[0][0] == 0:
            print("Solution found!")
            Printgrid(fitness_scores[0][1])
            return
        
        # Check for stagnation
        if fitness_scores[0][0] == best_fitness:
            stagnation_count += 1
        else:
            stagnation_count = 0
        best_fitness = fitness_scores[0][0]
        
        # If stagnation occurs for 20 generations, increase mutation rate
        if stagnation_count > 20:
            print("Stagnation detected, increasing mutation rate.")
            mutation_rate += 0.05  # Slight increase in mutation rate
        
        # Select top individuals (elitism)
        new_population = [ind for _, ind in fitness_scores[:10]]  # Keep top 10 individuals
        
        # Create offspring through crossover and mutation
        while len(new_population) < 25:
            parent1, parent2 = random.choices(population, k=2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:  # Mutation chance is now dynamic
                child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
    
    # Output the best individual after all generations
    print("Best solution after 500 generations:")
    Printgrid(fitness_scores[0][1])

# Run the algorithm
genetic_algorithm()