# LearnCodex

LearnCodex is a minimal repository used for learning and testing GitHub's Codex.
It provides a simple environment to experiment with Codex automation and tasks.

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Move into the project directory:
   ```bash
   cd learncodex
   ```
3. Explore the repository and try running Codex commands.

## Running `hello.py`

To execute the `hello.py` script, run the following command from the project root:

```bash
python hello.py
```

The program will prompt for your name and greet you. You can control the greeting
in two ways:

* **Configuration file** – Create a `config.json` file in the working directory
  containing a `greeting_prefix` entry. For example:
  ```json
  {
    "greeting_prefix": "Welcome"
  }
  ```
  When this file is present the greeting will use the configured prefix.
* **Command-line arguments** – The script accepts optional arguments:
  * `--name`: supply the name to greet without prompting for input.
  * `--greeting-prefix`: override both the default and any value provided in
    `config.json`.

Examples:

```bash
# Read name from input and use the prefix from config.json if available.
python hello.py

# Greet a specific person without prompting.
python hello.py --name Alice

# Override the greeting prefix supplied by config.json.
python hello.py --greeting-prefix "Salutations"
```

## Testing

This project uses **pytest** for its test suite. To run the tests:

```bash
pip install -r requirements.txt
pytest
```

Running `pytest` from the project root will execute all tests in the `tests/`
directory and report the results.
