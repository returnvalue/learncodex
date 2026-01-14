# LearnCodex

LearnCodex is a tiny Python project for practicing automation workflows. It
includes a single command-line program, its tests, and lightweight container
configs so you can experiment with running scripts, editing files, and
validating changes.

## Prerequisites

* Python 3.10 or newer. The code base uses modern typing syntax (e.g.
  `str | None`), so earlier versions of Python will not run the script.
* (Optional) A virtual environment if you prefer to isolate dependencies.
* (Optional) Docker and Docker Compose if you want to run the containerized
  version.

Install the project requirements with:

```bash
pip install -r requirements.txt
```

## Project layout

```
.
├── hello.py              # Main entry point for greeting users.
├── requirements.txt      # Runtime / test dependencies (pytest only).
├── Dockerfile            # Container image for running hello.py.
├── docker-compose.yml    # Compose setup for interactive runs.
└── tests/                # Automated tests for hello.py.
```

## Running `hello.py`

Execute the script from the project root:

```bash
python hello.py
```

By default the program prompts for a name, then prints a greeting using the
prefix "Hello". You can control both the name and greeting prefix in multiple
ways:

* **Environment variable** – Set `GREETING_PREFIX` to override the default.
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

When prompted for input, the script keeps asking until you provide a non-empty
name. If you pass an empty string via `--name`, the script prints a reminder and
exits without printing an incomplete greeting.

## Running with Docker

Build and run the container directly:

```bash
docker build -t learncodex .
docker run -it --rm -e GREETING_PREFIX=Howdy learncodex
```

Or use Docker Compose (interactive input is enabled by default):

```bash
docker compose run --rm learncodex
```

## Testing

The repository uses **pytest** for its tests. From the project root run:

```bash
pytest
```

This executes the suite in `tests/` and ensures both the command-line interface
and configuration logic behave as expected.
