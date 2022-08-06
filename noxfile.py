import nox
from nox_poetry import Session, session

nox.options.error_on_external_run = True
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["fmt_check", "lint", "type_check", "test"]


@session(python=["3.9", "3.10"])
def test(s: Session) -> None:
    s.install(".", "pytest", "pytest-cov", "pytest-check", "pytest-benchmark", "pyspark-test")
    s.run(
        "python",
        "-m",
        "pytest",
        "--cov=data_hack_faker",
        "--cov-report=html",
        "--cov-report=term",
        "tests",
        *s.posargs,
    )


@session(venv_backend="none")
def fmt(s: Session) -> None:
    s.run("isort", "src")
    s.run("black", "src")


@session(venv_backend="none")
def fmt_check(s: Session) -> None:
    s.run("isort", "--check", "src")
    s.run("black", "--check", "src")


@session(venv_backend="none")
def lint(s: Session) -> None:
    s.run("pflake8", "src")


@session(venv_backend="none")
def type_check(s: Session) -> None:
    s.run("mypy", "src", "tests", "noxfile.py")
