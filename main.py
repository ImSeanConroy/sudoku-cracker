import time
import argparse
from colorama import init, Fore

# Initialize colorama for cross-platform compatibility
init(autoreset=True)

class SudokuSolver:
    def __init__(self, original_board):
        self.original_board = original_board
        self.board = board = [row[:] for row in original_board]

    # Function to check if a number can be placed at board[row][col]
    def is_valid(self, row, col, num):
        # Check if the number is in the row or column
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
            
        # Check if the number is in the same 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    # Function to solve the Sudoku using backtracking
    def solve_sudoku(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    # Try numbers from 1 to 9
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num

                            if self.solve_sudoku():
                                return True
                            
                            self.board[row][col] = 0
                    return False
        return True

    # Function to print the Sudoku board
    def print_board(self, color_output=True):
        for row in range(9):
            for col in range(9):
                if self.original_board[row][col] != 0:
                    print(Fore.WHITE + str(self.board[row][col]) if color_output else str(self.board[row][col]), end=" ")
                elif self.board[row][col] != 0:
                    print(Fore.BLUE + str(self.board[row][col]) if color_output else str(self.board[row][col]), end=" ")
                else:
                    print('.', end=" ")
            print("")

# Function to parse user input for Sudoku puzzle from 3x3 cubes
def parse_cubes(cube_strs):
    try:
        # Convert 9 input strings (each for a 3x3 cube) into a 9x9 grid
        if len(cube_strs) != 9:
            raise ValueError("Must provide exactly 9 cubes.")
        
        board = [[0]*9 for _ in range(9)]  # Initialize empty 9x9 board

        for cube_idx, cube in enumerate(cube_strs):
            cube_rows = cube.split(",")
            if len(cube_rows) != 9:
                raise ValueError(f"cube {cube_idx} must have exactly 9 numbers.")
            
            # Map the cube to the right position in the full 9x9 grid
            row_offset, col_offset = 3 * (cube_idx // 3), 3 * (cube_idx % 3)
            for i in range(3):
                for j in range(3):
                    board[row_offset + i][col_offset + j] = int(cube_rows[i * 3 + j])

        return board
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Error parsing cubes: {str(e)}")

if __name__ == "__main__":
    # Command line argument parsing
    parser = argparse.ArgumentParser(description="Sudoku Cracker - Sit back, relax, and let your Sudoku puzzles be solved using brute-force.")
    parser.add_argument('--cubes', nargs=9, help='Enter 9 cubes as 3x3 groups')
    parser.add_argument('--no-color', action='store_false', help='Disable color output')
    parser.add_argument('--no-runtime', action='store_false', help='Disable runtime display')
    
    args = parser.parse_args()

    original_board = parse_cubes(args.cubes)
    start_time = time.time()
    solver = SudokuSolver(original_board)

    print("\nOriginal Puzzle:")
    solver.print_board(color_output=args.no_color)

    # Solve the puzzle
    if solver.solve_sudoku():
        end_time = time.time()
        print("\nSolved Puzzle:")
        solver.print_board(color_output=args.no_color)
        print("")

        if args.no_runtime:
            print(f"Run time: {end_time - start_time:.4f} seconds\n")
    else:
        print("No solution exists.")