# pytest-bdd exercise project

This project uses pytest-bdd as main tool for running automated test cases for http://www.automationpractice.pl/index.php

Tests cases cover several functionalities related to:
- Login
- Registering an account
- Shopping flow
- Product filtering and sorting

### Setup

The project requires from user to have Firefox installed beforehand. The driver for Firefox will be automatically downloaded when running tests for the first time.

Firstly, make a virtual environment:
`python -m venv your_venv`

Make sure to activate it straight away: `your_venv\Scripts\activate`. Your handle should now start with `(your_venv)`.

Secondly, install dependencies:
`pip install -r requirements.txt`

The packages you just installed are contained within `your_venv` virtual environment.


Everything should be set up to run tests:
`pytest tests --html=reports/report.html`

**Note:** There are 4 tests expected to fail every time, as they relate to one bugged feature. There may also be a few other cases that will fail with `StaleElementReferenceException`. This is a documented bug, more about it in `test_item_sort_filter.py, line 57`.
