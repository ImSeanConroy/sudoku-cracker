import pytest
from utils import parse_cubes, parse_rows, validate_input

def test_valid_cube_input():
  """Test a valid cube input."""
  input = [
    "003500160",
    "029700005",
    "100000009",
    "049000050",
    "000006010",
    "000250006",
    "000008000",
    "050037000",
    "080002001",
  ]
  board = parse_cubes(input)
  assert board == [
    [0, 0, 3, 0, 2, 9, 1, 0, 0],
    [5, 0, 0, 7, 0, 0, 0, 0, 0],
    [1, 6, 0, 0, 0, 5, 0, 0, 9],
    [0, 4, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 2, 5, 0],
    [0, 5, 0, 0, 1, 0, 0, 0, 6],
    [0, 0, 0, 0, 5, 0, 0, 8, 0],
    [0, 0, 8, 0, 3, 7, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
  ]

def test_invalid_cube_input():
  """Test a invalid cube input."""
  input = [
    "003500160",
    "0297000",
    "100000009",
    "04900005",
    "000006010",
    "0002506",
    "000008000",
    "05003700",
    "080002001",
  ]
  # board = parse_cubes(input)
  with pytest.raises(ValueError):
    parse_cubes(input)

def test_valid_row_input():
  """Test a valid row input."""
  input = [
    "003029100",
    "500700000",
    "160005009",
    "049000000",
    "000006250",
    "050010006",
    "000050080",
    "008037002",
    "000000001",
  ]
  board = parse_rows(input)
  assert board == [
    [0, 0, 3, 0, 2, 9, 1, 0, 0],
    [5, 0, 0, 7, 0, 0, 0, 0, 0],
    [1, 6, 0, 0, 0, 5, 0, 0, 9],
    [0, 4, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 2, 5, 0],
    [0, 5, 0, 0, 1, 0, 0, 0, 6],
    [0, 0, 0, 0, 5, 0, 0, 8, 0],
    [0, 0, 8, 0, 3, 7, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
  ]

def test_invalid_row_input():
  """Test a invalid row input."""
  input = [
    "0030290",
    "500700000",
    "160005009",
    "0490000",
    "000006250",
    "05010006",
    "000050080",
    "0037002",
    "000000001",
  ]
  # board = parse_cubes(input)
  with pytest.raises(ValueError):
    parse_rows(input)

def test_validate_input_valid():
    """Valid input with exactly 9 strings of 9 characters each"""
    validate_input(["123456789"] * 9)

def test_validate_input_too_few_strings():
    """Less than 9 strings"""
    with pytest.raises(ValueError, match="Must provide exactly 9 input strings."):
        validate_input(["123456789"] * 8)

def test_validate_input_too_many_strings():
    """More than 9 strings"""
    with pytest.raises(ValueError, match="Must provide exactly 9 input strings."):
        validate_input(["123456789"] * 10)

def test_validate_input_string_too_short():
    """One string with fewer than 9 characters"""
    with pytest.raises(ValueError, match="Input string 0 must have exactly 9 characters."):
        validate_input(["12345678"] + ["123456789"] * 8)

def test_validate_input_string_too_long():
    """One string with more than 9 characters"""
    with pytest.raises(ValueError, match="Input string 0 must have exactly 9 characters."):
        validate_input(["1234567890"] + ["123456789"] * 8)
