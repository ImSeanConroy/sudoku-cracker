import time
from colorama import init, Fore

init(autoreset=True)

# Function to check if a number can be placed at board[row][col]
def is_valid(board, row, col, num):
    # Check if the number is in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is in the column
    for i in range(9):
        if board[i][col] == num:
            return False
        
    # Check if the number is in the same 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Function to solve the Sudoku using backtracking
def solve_sudoku(board, original_board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        if solve_sudoku(board, original_board):
                            return True
                        
                        board[row][col] = 0
                return False
    return True

# Function to print the Sudoku board
def print_board(board, original_board):
    for row in range(9):
        for col in range(9):
            if original_board[row][col] != 0:
                print(Fore.WHITE + str(board[row][col]), end=" ")
            elif board[row][col] != 0:
                print(Fore.BLUE + str(board[row][col]), end=" ")
            else:
                print('.', end=" ")
        print("")

if __name__ == "__main__":
    # Sudoku puzzle
    original_board = [
        [0, 0, 3, 0, 2, 9, 1, 0, 0],
        [5, 0, 0, 7, 0, 0, 0, 0, 0],
        [1, 6, 0, 0, 0, 5, 0, 0, 9],
        [0, 4, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 2, 5, 0],
        [0, 5, 0, 0, 1, 0, 0, 0, 6],
        [0, 0, 0, 0, 5, 0, 0, 8, 0],
        [0, 0, 8, 0, 3, 7, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 1]
    ]

    # Make a copy of the original board
    board = [row[:] for row in original_board]

    # Start the timer
    start_time = time.time()

    print("\nOriginal Puzzle:")
    print_board(original_board, original_board)

    # Solve the Sudoku
    if solve_sudoku(board, original_board):
        # End the timer and calculate run time
        end_time = time.time()
        run_time = end_time - start_time

        print("\nSolved Puzzle:")
        print_board(board, original_board)
        print(f"\nRun time: {run_time:.4f} seconds\n")
    else:
        print("No solution exists.")