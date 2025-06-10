import subprocess
import sys
from pathlib import Path


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
