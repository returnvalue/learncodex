import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from hello import greet_user


def run_hello_script(
    input_text: str,
    args: list[str] | None = None,
    cwd: Path | None = None,
) -> subprocess.CompletedProcess[str]:
    """Execute hello.py with *input_text* and return the completed process."""

    script = PROJECT_ROOT / "hello.py"
    command = [sys.executable, str(script)]
    if args:
        command.extend(args)
    return subprocess.run(
        command,
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
        cwd=cwd,
    )


def test_hello_script():
    result = run_hello_script('Tester\n')
    # The program first prompts for the user's name and then prints the greeting.
    # We only care that the greeting appears at the end of the output.
    output_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert output_lines[-1].endswith('Hello, Tester!')


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
    result = run_hello_script('\nBob\n')
    output_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert output_lines[-1].endswith('Hello, Bob!')
    assert 'Please enter a valid name.' in result.stdout


def test_cli_name_skips_prompt():
    """Providing --name should avoid prompting for input."""

    result = run_hello_script('', ['--name', 'Eve'])
    output_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert output_lines[-1] == 'Hello, Eve!'
    assert 'What is your name?' not in result.stdout


def test_greet_user_custom_prefix_from_config(monkeypatch, capsys, tmp_path):
    """greet_user should read prefix from config.json when provided."""
    (tmp_path / 'config.json').write_text('{"greeting_prefix": "Welcome"}')
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr('builtins.input', lambda _='': 'Charlie')
    greet_user()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Welcome, Charlie!'


def test_hello_script_prefers_config_prefix(tmp_path):
    """Ensure hello.py uses the greeting prefix provided by config.json."""

    prefix = 'Greetings'
    (tmp_path / 'config.json').write_text('{"greeting_prefix": "Greetings"}')
    result = run_hello_script('Dana\n', cwd=tmp_path)
    output_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert output_lines[-1].endswith(f'{prefix}, Dana!')
    assert 'Hello, Dana!' not in result.stdout


def test_cli_overrides_config_prefix(tmp_path):
    """Command-line prefix should override config.json values."""

    (tmp_path / 'config.json').write_text('{"greeting_prefix": "Hi"}')
    result = run_hello_script(
        '',
        ['--name', 'Frank', '--greeting-prefix', 'Salutations'],
        cwd=tmp_path,
    )
    output_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert output_lines[-1] == 'Salutations, Frank!'


def test_main_passes_cli_arguments(monkeypatch):
    """Ensure hello.main forwards CLI args to greet_user."""

    captured: dict[str, str | None] = {}

    def fake_greet_user(
        prefix: str | None = None,
        name: str | None = None,
        config_path: str | Path = 'config.json',
    ) -> None:
        captured['prefix'] = prefix
        captured['name'] = name
        captured['config_path'] = str(config_path)

    monkeypatch.setattr('hello.greet_user', fake_greet_user)
    monkeypatch.setattr(
        sys,
        'argv',
        ['hello.py', '--name', 'Zoe', '--greeting-prefix', 'Hola'],
    )

    from hello import main

    main()

    assert captured['name'] == 'Zoe'
    assert captured['prefix'] == 'Hola'
    assert captured['config_path'].endswith('config.json')


def test_main_cli_overrides_config(monkeypatch, capsys, tmp_path):
    """hello.main should honour CLI arguments even when config.json exists."""

    (tmp_path / 'config.json').write_text('{"greeting_prefix": "Config"}')
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        sys,
        'argv',
        ['hello.py', '--name', 'Ivy', '--greeting-prefix', 'Salute'],
    )

    from hello import main

    main()

    captured = capsys.readouterr()
    assert 'Salute, Ivy!' in captured.out
    assert 'Config, Ivy!' not in captured.out
