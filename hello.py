import argparse
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def load_config(config_path: Path | str = "config.json") -> dict:
    """Load configuration from *config_path*.

    If the file does not exist or contains invalid JSON, an empty
    configuration is returned.
    """
    path = Path(config_path)
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        logger.info("Config file %s not found, using defaults", path)
    except json.JSONDecodeError:
        logger.warning("Config file %s is invalid JSON, using defaults", path)
    return {}


def greet_user(
    prefix: str | None = None,
    name: str | None = None,
    config_path: Path | str = "config.json",
) -> None:
    """Prompt for a user's name and greet them.

    Continues prompting until a non-empty name is provided unless *name* is
    supplied.
    """

    if prefix is None:
        config = load_config(config_path)
        prefix = config.get("greeting_prefix", "Hello")

    if name is not None:
        name = name.strip()
        if not name:
            logger.warning("Provided name is empty after stripping whitespace")
            print("Please enter a valid name.")
            return
        logger.info("User greeted with name: %s", name)
        print(f"{prefix}, {name}!")
        return

    while True:
        response: str = input("What is your name? ").strip()
        if response:
            logger.info("User greeted with name: %s", response)
            name = response
            break
        logger.warning("User entered an empty name")
        print("Please enter a valid name.")
    print(f"{prefix}, {name}!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet the user")
    parser.add_argument("--name", help="Name of the person to greet")
    parser.add_argument(
        "--greeting-prefix",
        dest="greeting_prefix",
        help="Greeting prefix to use instead of reading from config.json",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    greet_user(prefix=args.greeting_prefix, name=args.name)


if __name__ == "__main__":
    main()
