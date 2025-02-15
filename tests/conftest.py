import os
from datetime import datetime
from zipfile import ZipFile

import requests
from pytest import fixture, hookimpl
from selenium.webdriver import Firefox, FirefoxOptions, FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver

from conf.paths import drivers_dir, geckodriver_exe_path, geckodriver_zip_path, screenshots_dir
from conf.urls import GECKODRIVER_URL

@fixture
def driver():
    options = FirefoxOptions()
    options.add_argument("--headless")
    service = FirefoxService(executable_path=geckodriver_exe_path)
    firefox = Firefox(options=options, service=service)
    firefox.maximize_window()
    yield firefox
    firefox.close()
    firefox.quit()


@fixture(autouse=True, scope="session")
def download_driver():
    if os.path.isfile(geckodriver_exe_path):
        return

    response = requests.get(GECKODRIVER_URL, stream=True)

    with open(geckodriver_zip_path, mode="wb") as file:
        for chunk in response.iter_content(chunk_size=10 * 1024):  # 10 kilobytes
            file.write(chunk)

    with ZipFile(geckodriver_zip_path, "r") as zipped_driver:
        zipped_driver.extractall(drivers_dir)


@hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Lots of boilerplate only to..."""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            screenshot_path = attach_screenshot(item)  # ...attach screenshots.
            extras.append(pytest_html.extras.image(screenshot_path))
        report.extras = extras

def attach_screenshot(item):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    request = item.funcargs['request']
    driver: WebDriver = request.getfixturevalue('driver')
    screenshot_path = os.path.join(screenshots_dir, f"{timestamp}.png")
    os.makedirs(screenshots_dir, exist_ok=True)
    driver.get_full_page_screenshot_as_file(screenshot_path)
    return os.path.join("screenshots", f"{timestamp}.png")
