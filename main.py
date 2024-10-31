import time
import argparse
from sudoku_cracker import SudokuCracker
from utils import parse_cubes, parse_rows, read_from_file

def main():
    """Main function to run the Sudoku Cracker."""
    parser = argparse.ArgumentParser(description="Sudoku Cracker - Solve Sudoku puzzles using brute-force.")
    parser.add_argument('--file', type=str, help='File path to puzzle text file')
    parser.add_argument('--cubes', nargs=9, help='Enter 9 cubes as 3x3 groups')
    parser.add_argument('--rows', nargs=9, help='Enter 9 rows')
    parser.add_argument('--no-color', action='store_false', help='Disable color output')
    parser.add_argument('--no-runtime', action='store_false', help='Disable runtime display')
    parser.add_argument('--no-seperators', action='store_true', help='Disable Column and Row Seperators')
    
    args = parser.parse_args()
    
    original_board = [[0 for _ in range(9)] for _ in range(9)]

    if args.file:
        original_board = read_from_file(args.file)
    elif args.cubes:
        original_board = parse_cubes(args.cubes)
    elif args.rows:
        original_board = parse_rows(args.rows)
    else:
        print("Please provide either a puzzle file or 9 cubes.")
        exit(1)

    solver = SudokuCracker(original_board, color_output=args.no_color, no_seperators=args.no_seperators, show_progress=args.show_progress)

    print("\nOriginal Puzzle:")
    solver.print_board()

    start_time = time.time()
    if solver.solve_sudoku():
        end_time = time.time()
        print("\nSolved Puzzle:")
        solver.print_board()
        print("")

        if args.no_runtime:
            print(f"Run time: {end_time - start_time:.4f} seconds\n")
    else:
        print("\nNo solution exists.\n")

if __name__ == "__main__":
    main()
