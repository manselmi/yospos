import pytest
from typer.testing import CliRunner

from manselmi.yospos.app import app

runner = CliRunner()


@pytest.mark.parametrize(
    ("args", "exit_code"),
    [
        ([], 0),
    ],
)
def test_app(args, exit_code):
    result = runner.invoke(app, args)
    assert result.exit_code == exit_code
