import time
import argparse
from sudoku_cracker import SudokuCracker
from utils import parse_cubes

def main():
    """Main function to run the Sudoku Cracker."""
    parser = argparse.ArgumentParser(description="Sudoku Cracker - Solve Sudoku puzzles using brute-force.")
    parser.add_argument('--cubes', nargs=9, help='Enter 9 cubes as 3x3 groups')
    parser.add_argument('--no-color', action='store_false', help='Disable color output')
    parser.add_argument('--no-runtime', action='store_false', help='Disable runtime display')

    args = parser.parse_args()
    
    original_board = parse_cubes(args.cubes)
    solver = SudokuCracker(original_board)

    print("\nOriginal Puzzle:")
    solver.print_board(color_output=args.no_color)

    start_time = time.time()
    if solver.solve_sudoku():
        end_time = time.time()
        print("\nSolved Puzzle:")
        solver.print_board(color_output=args.no_color)
        print("")

        if args.no_runtime:
            print(f"Run time: {end_time - start_time:.4f} seconds\n")
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
