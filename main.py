
from maze import Maze


def select_difficulty():
    """Allow the user to select a maze difficulty."""

    print("\nSelect Difficulty")
    print("1. Easy   (9 x 9)")
    print("2. Medium (15 x 15)")
    print("3. Hard   (21 x 21)")

    while True:
        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            return 9, 9
        elif choice == '2':
            return 15, 15
        elif choice == '3':
            return 21, 21
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def main():
    print("\n================================")
    print("       MAZE GENERATOR")
    print("================================")

    rows, cols = select_difficulty()

    maze = Maze(rows, cols)
    maze.generate()

    print(f"\nGenerated Maze: {rows} x {cols}")
    print("S = Start | E = Exit | | = Wall")
    print("Spaces represent accessible paths.\n")

    maze.display()


if __name__ == "__main__":
    main()

