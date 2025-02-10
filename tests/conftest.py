import os
from zipfile import ZipFile

import requests
from pytest import fixture
from selenium.webdriver import Firefox, FirefoxOptions, FirefoxService

from conf.paths import drivers_dir, geckodriver_exe_path, geckodriver_zip_path
from conf.urls import GECKODRIVER_URL

@fixture
def driver(download_driver):
    options = FirefoxOptions()
    # options.add_argument("--headless")
    service = FirefoxService(executable_path=geckodriver_exe_path)
    firefox = Firefox(options=options, service=service)
    firefox.maximize_window()
    yield firefox
    firefox.close()
    firefox.quit()


@fixture
def download_driver():
    if os.path.isfile(geckodriver_exe_path):
        return

    response = requests.get(GECKODRIVER_URL, stream=True)

    with open(geckodriver_zip_path, mode="wb") as file:
        for chunk in response.iter_content(chunk_size=10 * 1024):  # 10 kilobytes
            file.write(chunk)

    with ZipFile(geckodriver_zip_path, "r") as zipped_driver:
        zipped_driver.extractall(drivers_dir)