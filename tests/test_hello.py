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
