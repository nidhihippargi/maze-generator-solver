
from maze import Maze
from player import Player


def select_difficulty():
    """Allow the user to select a maze difficulty."""

    print("\nSelect Difficulty")
    print("1. Easy   (15 x 15)")
    print("2. Medium (21 x 21)")
    print("3. Hard   (31 x 31)")

    while True:
        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            return 7, 7
        elif choice == '2':
            return 10, 10
        elif choice == '3':
            return 15, 15
        else:
            print("Invalid choice. Please try again.")


def play_game(maze, player):
    """Run the maze navigation game."""

    print("\nUse W, A, S, D to move.")
    print("Enter B to view the BFS solution.")
    print("Enter Q to quit the game.")

    while not player.has_won(maze):

        print("\n")
        maze.display(player.position)

        print(f"\nPlayer: {player.name}")
        print(f"Moves: {player.moves}")

        direction = input("Your move: ").strip().upper()

        if direction == 'Q':
            print("\nGame exited.")
            return
        if direction == 'B':
            path = maze.solve()
            maze.display_solution(path)

        if path:
            print("\nShortest path moves:", len(path) - 1)

        continue
    player.move(direction, maze)

    print("\n")
    maze.display(player.position)

    print("\n================================")
    print("       MAZE COMPLETED!")
    print("================================")
    print(f"Player: {player.name}")
    print(f"Total moves: {player.moves}")


def main():
    print("\n================================")
    print("       MAZE GENERATOR")
    print("================================")

    name = input("\nEnter your name: ").strip()

    if not name:
        name = "Player"

    rows, cols = select_difficulty()

    maze = Maze(rows, cols)
    maze.generate()

    player = Player(name, maze.start)

    play_game(maze, player)


if __name__ == "__main__":
    main()
