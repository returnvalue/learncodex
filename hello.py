import logging

logger = logging.getLogger(__name__)


def greet_user() -> None:
    """Prompt for a user's name and greet them.

    Continues prompting until a non-empty name is provided.
    """
    while True:
        name: str = input("What is your name? ").strip()
        if name:
            logger.info("User greeted with name: %s", name)
            break
        logger.warning("User entered an empty name")
        print("Please enter a valid name.")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    greet_user()
