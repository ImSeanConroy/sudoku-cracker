import pytest
from utils import parse_cubes, parse_rows

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