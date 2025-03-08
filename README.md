# Sudoku Solver using Genetic Algorithm

This project implements a Sudoku solver using a Genetic Algorithm. The AI optimizes solutions by applying evolutionary techniques such as selection, crossover, and mutation while ensuring adherence to Sudoku constraints.

## Features
- Uses a **genetic algorithm** to solve Sudoku puzzles.
- Implements **crossover and mutation** for optimization.
- **Dynamic mutation rate** to overcome stagnation.
- Displays the best solution found.

## Requirements
- Python 3.x
- No external dependencies are required.

## How It Works
1. Initializes a random population of Sudoku grids.
2. Evaluates fitness based on row, column, and subgrid constraints.
3. Uses **elitism** to retain the best individuals.
4. Applies **crossover** by swapping random 3x3 subgrids between parents.
5. Applies **mutation** to introduce random changes.
6. If no improvement is observed for 20 generations, the mutation rate increases.
7. The algorithm stops if a valid Sudoku solution is found or after 500 generations.

## Usage
Run the script using:
```bash
python sudoku_solver.py
```

## Output Example
```
Generation 1: Best Fitness = 52
Generation 2: Best Fitness = 45
...
Solution found!
|--------------------------------|
|  5 3 4 | 6 7 8 | 9 1 2 |
|  6 7 2 | 1 9 5 | 3 4 8 |
|  1 9 8 | 3 4 2 | 5 6 7 |
|----------+----------+----------|
|  8 5 9 | 7 6 1 | 4 2 3 |
|  4 2 6 | 8 5 3 | 7 9 1 |
|  7 1 3 | 9 2 4 | 8 5 6 |
|----------+----------+----------|
|  9 6 1 | 5 3 7 | 2 8 4 |
|  2 8 7 | 4 1 9 | 6 3 5 |
|  3 4 5 | 2 8 6 | 1 7 9 |
|--------------------------------|
```

## Customization
- Modify `initialize_population(size)` to change the population size.
- Adjust `generations` in `genetic_algorithm()` to control how many iterations the algorithm runs.
- Tune `mutation_rate` for different mutation probabilities.

## Author
Moaaz Mohamed Salama

## License
This project is open-source and available under the MIT License.

