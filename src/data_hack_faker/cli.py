from pathlib import Path
from typing import Optional

import typer

app = typer.Typer()


@app.command()
def run(
    size: int = typer.Option(1000, "--size", "-s"),  # noqa: B008
    verbose: bool = typer.Option(False, "--verbose", "-v"),  # noqa: B008
    out: Optional[Path] = typer.Option(None, "--output", "-o"),  # noqa: B008
):
    typer.echo(f"Table size: {size} rows")
    typer.echo(f"Verbosity: {verbose}")
    typer.echo(f"Output file: {out}")


if __name__ == "__main__":
    app()
