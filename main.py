
from maze import Maze


def main():
    print("\n==============================")
    print("      MAZE GENERATOR")
    print("==============================\n")

    maze = Maze(9, 9)
    maze.generate()

    print("S = Start | E = Exit | | = Wall\n")
    maze.display()


if __name__ == "__main__":
    main()
