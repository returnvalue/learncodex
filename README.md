# LearnCodex

LearnCodex is a tiny Python project that exists purely for practicing automation
workflows. The repository contains a single command line program, its tests, and
a dependency list so you can experiment with running tasks such as executing
scripts, editing files, and validating changes.

## Prerequisites

* Python 3.10 or newer. The code base uses modern typing syntax (e.g. `str | None`),
  so earlier versions of Python will not run the script.
* (Optional) A virtual environment if you prefer to isolate dependencies.

Install the project requirements with:

```bash
pip install -r requirements.txt
```

## Project layout

```
.
├── hello.py         # Main entry point for greeting users.
├── requirements.txt # Runtime / test dependencies (pytest only).
└── tests/           # Automated tests for hello.py.
```

## Running `hello.py`

Execute the script from the project root:

```bash
python hello.py
```

By default the program prompts for a name, then prints a greeting using the
prefix "Hello". You can control both the name and greeting prefix:

* **Configuration file** – If a `config.json` file exists in the current working
  directory the script reads a `greeting_prefix` value from it. Example:

  ```json
  {
    "greeting_prefix": "Welcome"
  }
  ```

  The configuration file is optional; if it is missing or contains invalid JSON
  the program falls back to the default prefix.
* **Command-line arguments** – `hello.py` exposes two optional flags:
  * `--name`: provide the name to greet without prompting for input.
  * `--greeting-prefix`: override both the default and any value supplied by
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

If you pass an empty string via `--name` or enter only whitespace when prompted
the script reminds you to enter a valid name and exits without printing an
incomplete greeting.

## Testing

The repository uses **pytest** for its tests. From the project root run:

```bash
pytest
```

This executes the suite in `tests/` and ensures both the command line interface
and configuration logic behave as expected.
