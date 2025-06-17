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


def greet_user(prefix: str | None = None, config_path: Path | str = "config.json") -> None:
    """Prompt for a user's name and greet them.

    Continues prompting until a non-empty name is provided.
    """
    if prefix is None:
        config = load_config(config_path)
        prefix = config.get("greeting_prefix", "Hello")

    while True:
        name: str = input("What is your name? ").strip()
        if name:
            logger.info("User greeted with name: %s", name)
            break
        logger.warning("User entered an empty name")
        print("Please enter a valid name.")
    print(f"{prefix}, {name}!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    greet_user()
