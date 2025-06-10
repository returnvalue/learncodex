def greet_user() -> None:
    """Prompt for a user's name and greet them."""
    name: str = input("What is your name? ")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet_user()
