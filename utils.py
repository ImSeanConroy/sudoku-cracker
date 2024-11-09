import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt

def validate_input(input_strs):
    """Ensure that exactly 9 strings are provided, and each has exactly 9 characters."""
    if not isinstance(input_strs, list) or len(input_strs) != 9:
        raise ValueError("Must provide exactly 9 input strings.")
    
    for idx, s in enumerate(input_strs):
        if not isinstance(s, str):
            raise TypeError(f"Input {idx} is not a string.")
        if len(s) != 9:
            raise ValueError(f"Input string {idx} must have exactly 9 characters.")
        if not s.isdigit():
            raise ValueError(f"Input string {idx} must contain only digits.")

def parse_cubes(cube_strs):
    """Convert 9 input strings (each representing a 3x3 cube) into a 9x9 grid."""
    validate_input(cube_strs)
    
    board = [[0] * 9 for _ in range(9)]
    try:
        for cube_idx, cube in enumerate(cube_strs):
            row_offset, col_offset = 3 * (cube_idx // 3), 3 * (cube_idx % 3)
            for i in range(3):
                for j in range(3):
                    board[row_offset + i][col_offset + j] = int(cube[i * 3 + j])    
    except ValueError as e:
        raise ValueError(f"Error converting cube {cube_idx}: {e}")
    return board

def parse_rows(row_strs):
    """Convert 9 input strings (each representing a row) into a 9x9 grid."""
    validate_input(row_strs)
    
    board = [[0] * 9 for _ in range(9)]
    try:
        for row_idx, row in enumerate(row_strs):
            for col_idx, char in enumerate(row):
                board[row_idx][col_idx] = int(char)
    except ValueError as e:
        raise ValueError(f"Error in row {row_idx}, column {col_idx}: {e}")
    return board

def read_from_file(file_path):
    """Reads a Sudoku puzzle from a specified text file."""
    board = []
    try:
        with open(file_path, 'r') as file:
            for line_idx, line in enumerate(file):
                values = line.split()
                if len(values) != 9:
                    raise ValueError(f"Line {line_idx + 1} must contain exactly 9 values.")
                board.append([int(v) for v in values])
        if len(board) != 9:
            raise ValueError("The file must contain exactly 9 lines.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except ValueError as e:
        print(f"Error reading file '{file_path}': {e}")
        return []
    return board

def read_from_image(img_path):
    """Reads a Sudoku puzzle from a specified image file."""
    try:
        print("\nPerforming Image Preprocessing...")
        preprocessed_image = preprocess_image(img_path)
        print("\nAttempting to Extract Digits...")
        board = extract_digits(preprocessed_image)
    except cv2.error as e:
        print(f"Error reading or processing image '{img_path}': {e}")
        return []
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return []
    return board

def preprocess_image(image_path):
    """Preprocesses image to grayscale and apply threshold."""
    img = cv2.imread(image_path, 0)
    if img is None:
        raise FileNotFoundError(f"Could not read the image file at '{image_path}'")
    
    if img.size == 0:
        raise ValueError(f"The image file '{image_path}' is empty or unreadable.")
    
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
            
            try:
                digit_str = pytesseract.image_to_string(resized_cell, config='--psm 10 digits').strip()
                if digit_str.isdigit():
                    board[i][j] = int(digit_str)
                else:
                    board[i][j] = 0  # Unable to detect a valid digit
            except pytesseract.TesseractError as e:
                print(f"Error processing cell ({i},{j}): {e}")
                board[i][j] = 0
    return board