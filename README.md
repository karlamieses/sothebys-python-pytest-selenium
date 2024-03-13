# Sothebys: python-pytest-selenium
This repository contains automation testing utilizing Python, Pytest and POM. 


### 👩🏽‍💻 Pre-requisites:
- [Install Python](https://www.python.org/ )
- [Install Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=mac)
- Install Pytest by running `pip install pytest`
  - You need to have installed `pip` or `pip3`, `pip3` is installed automatically if you're using Python3 
- Install Selenium by running this command `pip3 install selenium`

### How to run the tests?
- If you're using Pycharm, the test can run from the Play button
- If you want to run all the tests from the terminal:
  - Position yourself in the root folder, this will run all the tests within the "tests" folder Run the command `pytest`
    - **Note**: This is a sample test, if you run from the terminal the test `test_sign_up_page` will fail due to the 
    - user will be logged into the app from the test `test_log_in_page`, this will be improved.


### 💨 See recording of the test running:

Test No.1: `test_log_in_page.py`
A user will log into Sothebys, and will validate the redirection of the user
into the logged in account. 

Test No.2: `test_sign_up_page.py`
This test will validate the error message when attempting to signup with invalid email address

### 💨 What is out of the scopre of the tests?
- API testing
- CI/CD
- Reporting
- More tests (this is just a proof of concept)
