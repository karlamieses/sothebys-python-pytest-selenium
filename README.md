# Sothebys: python-pytest-selenium
This repository contains automation testing utilizing Python, Pytest and POM. 


### 👩🏽‍💻 Pre-requisites:
- Install Python
- Install Pycharm
- Install Pytest
- Install Selenium

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

👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽

[Screen Recording 2024-03-03 at 23.20.05.mov](..%2F..%2F..%2F..%2Fvar%2Ffolders%2F4k%2F80jzh6pd7zq1b44my74bwlsc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_LHUMeN%2FScreen%20Recording%202024-03-03%20at%2023.20.05.mov)

### 💨 What is out of the scopre of the tests?
- CI/CD
- Reporting
- More tests (this is just a proof of concept)
