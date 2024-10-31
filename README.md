# Sudoku Cracker

Sit back, relax, and let your Sudoku puzzles be solved using brute-force. This simple Python CLI tool allows you to input puzzles directly or provide a file path for automatic solving.

![Project Image](https://github.com/ImSeanConroy/sudoku-cracker/blob/main/.github/repo-img.png)


## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Development and Testing](#development-and-testing)
- [License](#license)
- [Support](#support)

## Getting Started

### Prerequisites

Before getting started, ensure you have the following installed:
- [Python](https://www.python.org/)

### Installation

The following contains instruction for getting this application running locally:

1. Clone the repository.
```bash
git clone https://github.com/ImSeanConroy/sudoku-cracker.git
cd sudoku-cracker
```

2. Create and start virtual environment
```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependencies
```bash
pip3 install -r requirements.txt
```

4. Run script
```bash
python main.py --cubes cube1 cube2 cube3 cube4 cube5 cube6 cube7 cube8 cube9
```

## Usage

The Sudoku Cracker allows you to input your Sudoku puzzle as 9 groups of 3x3 numbers. Each group represents a 3x3 cube, and the numbers are separated by commas. Use `0` for empty cells.

### Example Input

Solve puzzle from a set of cubes (input directly):

```bash
python main.py --cubes 003500160 029700005 100000009 049000050 000006010 000250006 000008000 050037000 080002001
```

### Additional Options

Solve puzzle from a file:
```bash
python main.py --file "example.txt"
```

Solve puzzle from a set of rows (input directly):
```bash
python main.py --rows "..."
```

Disable Color Output:
```bash
python main.py --cubes "..." --no-color
```

Disable Runtime Display:
```bash
python main.py --cubes "..." --no-runtime
```

Disable Column and Row Seperators:
```bash
python main.py --cubes "..." --no-seperators
```

## Development and Testing

1. Run the following command to run the full test suit:

```bash
pytest tests/
```

## License

This project is Distributed under the MIT License - see the [LICENSE](LICENSE) file for information.

## Support

If you are having problems, please let me know by [raising a new issue](https://github.com/ImSeanConroy/sudoku-cracker/issues/new/choose).
