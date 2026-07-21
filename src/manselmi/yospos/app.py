from typing import Annotated

import typer

YOSPOS = "yospos"


app = typer.Typer()


@app.command()
def main(*, shout: Annotated[bool, typer.Option("--shout")] = False) -> None:
    print(YOSPOS.upper() if shout else YOSPOS)  # noqa:T201


if __name__ == "__main__":
    app()
