# caffeine-py

Built using [cc-py](https://github.com/erujs/cc-py) `python-script` template.

## Dependencies

Ensure you have the following installed before getting started:

- **Python 3.10+** - required to develop and run the project
- **pytest** – for running tests

## Setup

### Step 1: Clone the generated project
```bash
git clone https://github.com/erujs/caffeine-py.git
cd caffeine-py
```

### Step 2: Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 3: Install the project
```bash
pip install -e ".[dev]"
```

## Usage

```bash
# Run directly
python -m caffeine_py.main

# Or if installed
caffeine_py
```

## Project Structure

```bash
caffeine-py/
├── caffeine_py/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── AGENTS.md
├── CLAUDE.md
├── pyproject.toml
└── README.md
```

## Test

```bash
pytest
```

✨ Happy coding!
If you find this project useful, a ⭐ on the repo is always appreciated!