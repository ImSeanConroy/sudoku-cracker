import pytest
from sudoku_cracker import SudokuCracker
from colorama import Fore

def test_initialization():
    """Test initialization with different configurations."""
    board = [[0] * 9 for _ in range(9)]
    solver = SudokuCracker(board, color_output=False, no_seperators=True)
    assert solver.color_output is False
    assert solver.no_seperators is True

def test_is_valid():
    """Test the is_valid function for correct placement validation."""
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solver = SudokuCracker(board)
    # Valid placement
    assert solver.is_valid(0, 2, 4) is True
    # Invalid row placement
    assert solver.is_valid(0, 2, 3) is False
    # Invalid column placement
    assert solver.is_valid(0, 2, 5) is False
    # Invalid subgrid placement
    assert solver.is_valid(1, 1, 9) is False

def test_solve_empty_board():
    """Test solving an empty board."""
    empty_board = [[0] * 9 for _ in range(9)]
    solver = SudokuCracker(empty_board)
    assert solver.solve_sudoku() is True
    # Check if the board is fully populated
    for row in solver.board:
        assert all(cell != 0 for cell in row)

def test_unsolvable_board():
    """Test a board that has no solution."""
    unsolvable_board = [
        [5, 5, 5, 0, 7, 0, 0, 0, 0],  # Invalid starting board (5 repeated)
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solver = SudokuCracker(unsolvable_board)
    assert solver.solve_sudoku() is False

def test_already_solved_board():
    """Test a board that is already solved."""
    solved_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    solver = SudokuCracker(solved_board)
    assert solver.solve_sudoku() is True 
    assert solver.board == solved_board

def test_print_board(capsys):
    """Test the print_board method for correct formatting."""
    original_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solver = SudokuCracker(original_board)
    solver.print_board()
    captured = capsys.readouterr().out
    assert captured.count('|') > 0
    assert captured.count('- - -') > 0