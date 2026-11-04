# Maze Generator & Solver

A terminal-based maze game developed using Python as part of the CS213 Introduction to Python Programming course at IIIT Raichur.

## Overview

The application generates random mazes and provides interactive gameplay, automatic shortest-path solving, and performance tracking. Players navigate through mazes, race against time, and compete for high scores on a persistent leaderboard.

## Features

- Random maze generation using Depth-First Search (DFS)
- Three difficulty levels:
  - Easy: 7 × 7 logical maze (15 × 15 grid)
  - Medium: 10 × 10 logical maze (21 × 21 grid)
  - Hard: 15 × 15 logical maze (31 × 31 grid)
- Player navigation using W, A, S, D keys
- Wall collision prevention
- Automatic shortest-path solving using Breadth-First Search (BFS)
- BFS solution path visualization
- Completion time and move tracking
- Score calculation based on moves and time
- Persistent JSON scoreboard with ranking

## Technologies Used

- Python
- `random` – randomized maze generation
- `time` – completion time tracking
- `json` – persistent scoreboard storage
- `collections.deque` – BFS traversal

## Project Structure

```text
maze-generator-solver/
├── main.py          # Application entry point and gameplay
├── maze.py          # Maze generation and BFS solver
├── player.py        # Player movement and navigation
├── scoreboard.py    # Score calculation and leaderboard
├── scoreboard.json  # Persistent score storage
└── README.md        # Project documentation
```

## Installation and Execution

Clone the repository:

```bash
git clone https://github.com/nidhihippargi/maze-generator-solver.git
```

Navigate into the project directory:

```bash
cd maze-generator-solver
```

Run the application:

```bash
python3 main.py
```

No external Python packages are required.

## Controls

| Key | Action |
|---|---|
| W | Move up |
| A | Move left |
| S | Move down |
| D | Move right |
| B | Display BFS shortest path |
| Q | Quit the current game |

Only valid player movements are counted.

## Scoring System

The score is calculated based on the number of moves and time taken to complete the maze.

```text
Score = 1000 - (Moves × 5) - (Time × 2)
```

The final score is converted to an integer and cannot fall below zero.

Completed games are stored in `scoreboard.json`. Scores are ranked in descending order, and the leaderboard persists across game sessions.

## Author

**Nidhi Hippargi**  
CS25B1030  
IIIT Raichur
