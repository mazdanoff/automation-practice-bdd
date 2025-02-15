import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

features_dir = os.path.join(project_path, "features")
tests_dir = os.path.join(project_path, "tests")

reports_dir = os.path.join(project_path, "reports")
screenshots_dir = os.path.join(reports_dir, "screenshots")

drivers_dir = os.path.join(project_path, "drivers")
geckodriver_zip_path = os.path.join(drivers_dir, "geckodriver.zip")
geckodriver_exe_path = os.path.join(drivers_dir, "geckodriver.exe")
chromedriver_zip_path = os.path.join(drivers_dir, "chromedriver.zip")
chromedriver_exe_path = os.path.join(drivers_dir, "chromedriver.exe")

