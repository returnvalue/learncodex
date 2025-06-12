def greet_user() -> None:
    """Prompt for a user's name and greet them.

    Continues prompting until a non-empty name is provided.
    """
    while True:
        name: str = input("What is your name? ").strip()
        if name:
            break
        print("Please enter a valid name.")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet_user()
