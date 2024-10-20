from colorama import init, Fore

# Initialize colorama for cross-platform compatibility
init(autoreset=True)

class SudokuCracker:
    def __init__(self, original_board):
        self.original_board = original_board
        self.board = [row[:] for row in original_board]

    def is_valid(self, row, col, num):
        """Check if a number can be placed at board[row][col]."""
        if num in self.board[row] or num in (self.board[i][col] for i in range(9)):
            return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku(self):
        """Solve the Sudoku using backtracking."""
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num

                            if self.solve_sudoku():
                                return True
                            
                            self.board[row][col] = 0  # Reset on backtrack
                    return False
        return True

    def print_board(self, color_output=True):
        """Print the Sudoku board with optional color output."""
        for row in range(9):
            for col in range(9):
                cell_value = self.board[row][col]
                if self.original_board[row][col] != 0:
                    print(Fore.WHITE + str(cell_value) if color_output else str(cell_value), end=" ")
                elif cell_value != 0:
                    print(Fore.LIGHTCYAN_EX + str(cell_value) if color_output else str(cell_value), end=" ")
                else:
                    print('.', end=" ")
            print("")  # New line after each row
