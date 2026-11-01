
class Player:
    """Represents a player navigating through a maze."""

    def __init__(self, name, start_position):
        self.name = name
        self.position = start_position
        self.moves = 0

    def move(self, direction, maze):
        """Move the player if the requested movement is valid."""

        # Map movement commands to coordinate changes
        directions = {
            'W': (-1, 0),
            'S': (1, 0),
            'A': (0, -1),
            'D': (0, 1)
        }

        direction = direction.upper()

        if direction not in directions:
            print("Invalid command! Use W, A, S or D.")
            return False

        # Calculate the new position
        dr, dc = directions[direction]

        new_row = self.position[0] + dr
        new_col = self.position[1] + dc

        # Check maze boundaries
        if not (0 <= new_row < maze.rows and
                0 <= new_col < maze.cols):
            print("You cannot move outside the maze!")
            return False

        # Check whether the destination is a wall
        if maze.grid[new_row][new_col] == '|':
            print("Blocked! There is a wall in that direction.")
            return False

        # Update player position
        self.position = (new_row, new_col)
        self.moves += 1

        return True

    def has_won(self, maze):
        """Check whether the player has reached the exit."""

        return self.position == maze.end
