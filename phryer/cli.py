from typer import Typer

from phryer.actions.dummy.cli import app as dummy_app
from phryer.actions.screenshot.cli import screenshot


def typer_app() -> Typer:
    app = Typer(pretty_exceptions_enable=False)

    app.add_typer(dummy_app, name="dummy")
    app.command()(screenshot)

    return app
