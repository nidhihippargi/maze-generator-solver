from collections import deque
import random


class Maze:
    """Generates and displays a random maze using DFS."""

    def __init__(self, rows, cols):
        if rows < 2 or cols < 2:
            raise ValueError("Logical dimensions must be at least 2.")

        # Convert logical dimensions to actual grid dimensions
        self.rows = 2 * rows + 1
        self.cols = 2 * cols + 1

        # Initially, every position is a wall
        self.grid = [
        ['|' for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

        self.start = (1, 1)
        self.end = (self.rows - 2, self.cols - 2)
    def generate(self):
        """Generate a maze using randomized DFS and backtracking."""

        stack = [self.start]

        # Mark starting position as a path
        r, c = self.start
        self.grid[r][c] = ' '

        while stack:
            r, c = stack[-1]

            # Possible movements: up, down, left, right
            directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            random.shuffle(directions)

            found = False

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check boundaries and whether the cell is unvisited
                if (1 <= nr < self.rows - 1 and
                    1 <= nc < self.cols - 1 and
                    self.grid[nr][nc] == '|'):

                    # Remove the wall between the two cells
                    wall_r = r + dr // 2
                    wall_c = c + dc // 2

                    self.grid[wall_r][wall_c] = ' '
                    self.grid[nr][nc] = ' '

                    # Move to the newly visited cell
                    stack.append((nr, nc))
                    found = True
                    break

            # Backtrack when no unvisited neighbour exists
            if not found:
                stack.pop()

        # Mark entrance and exit
        self.grid[self.start[0]][self.start[1]] = 'S'
        self.grid[self.end[0]][self.end[1]] = 'E'

    def solve(self):
        """Find the shortest path from start to exit using BFS."""

        queue = deque([self.start])

        visited = {self.start}
        predecessor = {self.start: None}

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        while queue:
            current = queue.popleft()

            # Exit reached
            if current == self.end:
                break

            r, c = current

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                neighbour = (nr, nc)

                # Check boundaries
                if not (0 <= nr < self.rows and
                        0 <= nc < self.cols):
                    continue

                # Check wall and visited status
                if self.grid[nr][nc] != '|' and neighbour not in visited:

                    visited.add(neighbour)
                    predecessor[neighbour] = current
                    queue.append(neighbour)

        # No path found
        if self.end not in predecessor:
            return None

        # Reconstruct path from exit to start
        path = []
        current = self.end

        while current is not None:
            path.append(current)
            current = predecessor[current]

        path.reverse()

        return path

    def display_solution(self, path):
        """Display the maze with the BFS solution path."""

        if path is None:
            print("No solution exists.")
            return

        solution_grid = [row[:] for row in self.grid]

        for r, c in path:
            if (r, c) != self.start and (r, c) != self.end:
                solution_grid[r][c] = '.'

        for row in solution_grid:
            print(' '.join(row))

    def display(self, player_position=None):
        """Display the maze and the player's current position."""

        for r in range(self.rows):
            row_display = []

            for c in range(self.cols):
                if player_position == (r, c):
                    row_display.append('P')
                else:
                    row_display.append(self.grid[r][c])

            print(' '.join(row_display))

