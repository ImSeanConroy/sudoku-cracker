# sudoku-cracker

Sit back, relax, and let your Sudoku puzzles be solved using brute-force.

<div>
  <p>
    <a href="https://github.com/ImSeanConroy/sudoku-cracker/issues">Report Bug</a>
    ·
    <a href="https://github.com/ImSeanConroy/sudoku-cracker/issues">Request Feature</a>
  </p>
</div>

## Table of Contents

- [sudoku-cracker](#sudoku-cracker)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
    - [Example Input](#example-input)
    - [Additional Options](#additional-options)
  - [License](#license)
  - [Support](#support)

## Getting Started

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
python main.py --cubes "cube1" "cube2" "cube3" "cube4" "cube5" "cube6" "cube7" "cube8" "cube9"
```

## Usage

The Sudoku Cracker allows you to input your Sudoku puzzle as 9 groups of 3x3 numbers. Each group represents a 3x3 cube, and the numbers are separated by commas. Use `0` for empty cells.

### Example Input
```bash
python main.py --cubes "0,0,3,0,2,9,1,0,0" "5,0,0,7,0,0,0,0,0" "1,6,0,0,0,5,0,0,9" "0,4,9,0,0,0,0,0,0" "0,0,0,0,0,6,2,5,0" "0,5,0,0,1,0,0,0,6" "0,0,0,0,5,0,0,8,0" "0,0,8,0,3,7,0,0,2" "0,0,0,0,0,0,0,0,1"
```

### Additional Options

Disable Color Output:
```bash
python main.py --cubes "..." --no-color
```

Disable Runtime Display:
```bash
python main.py --cubes "..." --no-runtime
```

## License

This project is Distributed under the MIT License - see the [LICENSE](LICENSE) file for information.

## Support

If you are having problems, please let me know by [raising a new issue](https://github.com/ImSeanConroy/sudoku-cracker/issues/new/choose).
