def parse_cubes(cube_strs):
    """Convert 9 input strings (each for a 3x3 cube) into a 9x9 grid."""
    if len(cube_strs) != 9:
        raise ValueError("Must provide exactly 9 cubes.")
    
    board = [[0] * 9 for _ in range(9)]

    for cube_idx, cube in enumerate(cube_strs):
        cube_rows = cube.split(",")
        if len(cube_rows) != 9:
            raise ValueError(f"Cube {cube_idx} must have exactly 9 numbers.")
        
        row_offset, col_offset = 3 * (cube_idx // 3), 3 * (cube_idx % 3)
        for i in range(3):
            for j in range(3):
                board[row_offset + i][col_offset + j] = int(cube_rows[i * 3 + j])

    return board

def read_from_file(file_path):
    """Reads a Sudoku puzzle from a specified text file."""
    board = []
    try:
        with open(file_path, 'r') as file:
            board = [list(map(int, line.split())) for line in file]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except ValueError:
        print("Error: The file contains non-integer values.")
        return []
    return board
