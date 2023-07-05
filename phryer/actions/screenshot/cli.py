import os

import typer
from loguru import logger

from phryer.actions.screenshot.controller import take_screenshot


def screenshot(
        url: str,
        save_location: str = typer.Option(
            str(os.getcwd()),
            "--save-location",
            "-l",
            help="Absolute path to save screenshot to. Defaults to CWD"
        )
):
    """
    Take a screenshot of a designated url
    """
    if not os.path.exists(save_location):
        logger.error("Save location does not exist!")
    take_screenshot(url, save_location)
