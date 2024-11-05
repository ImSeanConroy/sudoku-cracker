import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt

def validate_input(input_strs):
    """Ensure that exactly 9 strings are provided, and each has exactly 9 characters."""
    if len(input_strs) != 9:
        raise ValueError("Must provide exactly 9 input strings.")
    
    for idx, s in enumerate(input_strs):
        if len(s) != 9:
            raise ValueError(f"Input string {idx} must have exactly 9 characters.")

def parse_cubes(cube_strs):
    """Convert 9 input strings (each representing a 3x3 cube) into a 9x9 grid."""
    validate_input(cube_strs)
    
    board = [[0] * 9 for _ in range(9)]

    for cube_idx, cube in enumerate(cube_strs):
        row_offset, col_offset = 3 * (cube_idx // 3), 3 * (cube_idx % 3)
        for i in range(3):
            for j in range(3):
                board[row_offset + i][col_offset + j] = int(cube[i * 3 + j])    
    return board

def parse_rows(row_strs):
    """Convert 9 input strings (each representing a row) into a 9x9 grid."""
    validate_input(row_strs)
    
    board = [[0] * 9 for _ in range(9)]

    for row_idx, row in enumerate(row_strs):
        for col_idx, char in enumerate(row):
            board[row_idx][col_idx] = int(char)
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

def read_from_image(img_path):
    """Reads a Sudoku puzzle from a specified img file."""
    print("\nPerforming Image Preprocessing...")
    preprocessed_image = preprocess_image(img_path)

    print("\nAttempting to Extract Digits...")
    board = extract_digits(preprocessed_image)
    return board

def preprocess_image(image_path):
    """Preprocesses image to grayscale and apply threshold."""
    img = cv2.imread(image_path, 0)
    _, thresh = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    return thresh

def extract_digits(image, size=9):
    """Extract digits from the Sudoku image."""
    height, width = image.shape
    cell_h, cell_w = height // size, width // size

    board = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            cell = image[i * cell_h: (i + 1) * cell_h, j * cell_w: (j + 1) * cell_w]
            resized_cell = cv2.resize(cell, (100, 100))

            digit = pytesseract.image_to_string(resized_cell, config='--psm 10 digits')
            try:
                if digit.strip() != '':
                    board[i][j] = int(digit.strip())
            except ValueError:
                board[i][j] = 0
    return board