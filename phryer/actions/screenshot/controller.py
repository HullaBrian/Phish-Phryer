import os

import selenium.common.exceptions
from loguru import logger
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def take_screenshot(url: str, save_location: str) -> None:
    url_ = url.removeprefix("https://").removeprefix("http://").replace(".", "-")
    file_name = save_location + os.sep + url_.split("/")[0] + ".png"
    if save_location.endswith(os.sep) or "." in save_location.split(os.sep)[-1]:
        # save location is just a path, no file name
        file_name = save_location

    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    try:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    except selenium.common.exceptions.WebDriverException:
        driver = webdriver.Firefox(options=options)

    logger.info(f"URL: {url}, FILE NAME: {file_name}")
    driver.get(url)
    driver.save_full_page_screenshot(file_name)

    driver.quit()

    return True
