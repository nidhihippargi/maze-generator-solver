
import random


class Maze:
    """Generates and displays a random maze using DFS."""

    def __init__(self, rows, cols):
        if rows < 5 or cols < 5 or rows % 2 == 0 or cols % 2 == 0:
            raise ValueError("Dimensions must be odd and at least 5.")

        self.rows = rows
        self.cols = cols

        # Initially, every position is a wall
        self.grid = [['|' for _ in range(cols)] for _ in range(rows)]

        self.start = (1, 1)
        self.end = (rows - 2, cols - 2)

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

