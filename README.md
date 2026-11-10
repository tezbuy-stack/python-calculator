# Python Calculator

A clean, beginner-friendly command-line calculator written in Python 3. It does the six basic arithmetic operations, validates everything you type, and keeps a history of your calculations.

## Features

- **Six operations:** addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulo (`%`), and power (`**`)
- **Input validation:** non-numeric input is rejected with a friendly message instead of crashing
- **Safe division:** dividing by zero shows a clear error and lets you try again
- **Calculation history:** view every calculation from the current session
- **Simple menu:** pick an option, calculate, and quit cleanly
- **Zero dependencies:** Python standard library only

## Requirements

- Python 3.8 or newer

## Installation

```bash
git clone https://github.com/<your-username>/python-calculator.git
cd python-calculator
```

No packages to install — the project uses only the Python standard library.

## Usage

Run the calculator:

```bash
python3 calculator.py
```

Pick `1` for a new calculation, `2` to view history, and `3` to quit.

### Sample session

```
Welcome to the Python Calculator!
Do simple arithmetic, and type 3 in the menu to quit.

--- Calculator ---
1. New calculation
2. View history
3. Quit
------------------
Choose an option (1-3): 1
Enter the first number: 12
Enter an operator (+, -, *, /, %, **): *
Enter the second number: 4

Result: 12 * 4 = 48

--- Calculator ---
1. New calculation
2. View history
3. Quit
------------------
Choose an option (1-3): 1
Enter the first number: 10
Enter an operator (+, -, *, /, %, **): /
Enter the second number: 0
Error: cannot divide by zero. Please try again.

--- Calculator ---
1. New calculation
2. View history
3. Quit
------------------
Choose an option (1-3): 1
Enter the first number: abc
'abc' is not a valid number. Please try again.
Enter the first number: 7
Enter an operator (+, -, *, /, %, **): +
Enter the second number: 3

Result: 7 + 3 = 10

--- Calculator ---
1. New calculation
2. View history
3. Quit
------------------
Choose an option (1-3): 2

--- History ---
1. 12 * 4 = 48
2. 7 + 3 = 10
---------------

--- Calculator ---
1. New calculation
2. View history
3. Quit
------------------
Choose an option (1-3): 3

Thanks for using the calculator. Goodbye!
```

## How it works

- Each operation is a small function (`add`, `subtract`, `multiply`, `divide`, `modulo`, `power`) stored in an `OPERATIONS` dictionary keyed by its symbol, so adding a new operation is a one-line change.
- `read_number()` and `read_operator()` loop until the user enters valid input, so bad input never crashes the program.
- Division by zero is caught with a `try/except ZeroDivisionError` block.
- Every successful calculation is appended to an in-memory `history` list, which option `2` prints.

## Project structure

```
python-calculator/
├── calculator.py      # The calculator (CLI, standard library only)
├── README.md          # This file
├── requirements.txt   # No external dependencies
└── .gitignore         # Standard Python ignores
```

## License

MIT License — see [LICENSE](LICENSE) for details.
