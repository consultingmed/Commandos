# Maze Solver Under Partial Observability

A Python implementation of an A* search algorithm for finding a movement sequence that reaches a goal regardless of the agent's initial position.

## Problem Description

The agent moves through a grid-based maze containing walls, possible starting positions, and goal cells. Its exact initial position is unknown, but the set of possible starting positions is known.

The objective is to find a sequence of moves that guarantees reaching a goal from every possible starting position.

## Algorithm

### State Representation

Each search state is represented as a set of possible agent positions.

After a movement, the agent's position is updated from every position in the current set. Moves into walls leave the agent in place.

### A* Search

The solver uses A* to explore possible movement sequences and find a solution.

- Precomputes transitions between traversable cells for each movement direction.
- Represents sets of possible positions using immutable `frozenset` objects.
- Tracks the best known path length for each state to avoid redundant exploration.
- Uses a heuristic based on distances from possible positions to the nearest goal.

### Heuristic

Distances to goal cells are precomputed using multi-source breadth-first search (BFS).

For a state containing multiple possible positions, the heuristic takes the maximum of their individual distances to a goal. This estimates the minimum number of additional moves needed to bring all possible positions to goal cells.

## Input and Output

The program reads the maze from `zad_input.txt`.

- `#` represents a wall.
- `S` represents a possible starting position.
- `G` represents a goal.
- `B` represents a cell that is both a starting position and a goal.
- A space represents a traversable cell.

The resulting movement sequence is written to `zad_output.txt`, using `U`, `D`, `L`, and `R` for up, down, left, and right.

## Technologies

- Python
- A* search
- Breadth-first search (BFS)
- State-space search
- Precomputed transitions

## Running the Solver

Place the maze in `zad_input.txt` and run:

```bash
python komandos_A_star.py
```

The resulting movement sequence will be written to `zad_output.txt`.
