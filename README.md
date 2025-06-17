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


## Running hello.py

To execute the `hello.py` script, run the following command from the project root:

```bash
python hello.py
```

The program will prompt for your name and greet you. By default it uses the
prefix `"Hello"` but you can customise this by creating a `config.json` file in
the working directory containing a `greeting_prefix` entry. For example:

```json
{
  "greeting_prefix": "Welcome"
}
```

With this configuration, running `hello.py` will greet you with "Welcome".

## Testing

This project uses **pytest** for its test suite. To run the tests:

```bash
pip install -r requirements.txt
pytest
```

Running `pytest` from the project root will execute all tests in the `tests/` directory and report the results.
