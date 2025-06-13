import subprocess
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from hello import greet_user


def test_hello_script(tmp_path):
    script = Path(__file__).resolve().parents[1] / 'hello.py'
    result = subprocess.run(
        [sys.executable, str(script)],
        input='Tester\n',
        text=True,
        capture_output=True,
        check=True,
    )
    # The program first prompts for the user's name and then prints the greeting.
    # We only care that the greeting appears at the end of the output.
    assert result.stdout.strip().endswith('Hello, Tester!')


def test_greet_user(monkeypatch, capsys):
    """Ensure greet_user prints the expected greeting."""
    monkeypatch.setattr('builtins.input', lambda _='': 'Alice')
    greet_user()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Hello, Alice!'


def test_greet_user_empty_then_valid(monkeypatch, capsys):
    """Ensure greet_user reprompts when given an empty name."""
    responses = iter(['', 'Bob'])
    monkeypatch.setattr('builtins.input', lambda _='': next(responses))
    greet_user()
    captured = capsys.readouterr()
    output_lines = [line.strip() for line in captured.out.splitlines() if line.strip()]
    assert output_lines[-1] == 'Hello, Bob!'
    assert 'Please enter a valid name.' in output_lines

def test_hello_script_empty_then_valid(tmp_path):
    """Ensure the script reprompts on empty input."""
    script = Path(__file__).resolve().parents[1] / 'hello.py'
    result = subprocess.run(
        [sys.executable, str(script)],
        input='\nBob\n',
        text=True,
        capture_output=True,
        check=True,
    )
    output_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert output_lines[-1].endswith('Hello, Bob!')
    assert 'Please enter a valid name.' in result.stdout
