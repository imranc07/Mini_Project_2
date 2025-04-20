# Mini Project - 2

This project implements a Page Object Model (POM) structure for automated testing of the [HRM](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login).

Website Link: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login/


## Test Objective:

The objective of this project is to implement an automated testing framework for the [HRM](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) web application using Python Selenium. The primary goals are to:

- **Validate Functionalities:** Ensure the core functionalities of the HRM platform (such as navigation, login, and sign-up processes) work as expected.
- **Improve Test Maintenance:** Utilize a structured approach to separate web page interaction logic from test scripts, making it easier to maintain and extend as the application evolves.
- **Enhance Test Reusability:** Promote reusability of code for interactions with page elements, reducing duplication across test scripts.
- **Support Data-Driven Testing:** Leverage test data (stored in TestData/data.py and TestData/testdata.xlx) to run multiple test scenarios with different input sets to verify robustness and edge case handling.
- **Increase Test Coverage:** Automate critical paths such as user authentication, button functionality, and error handling to ensure high test coverage across essential user flows.
- **Ensure Browser Compatibility:** Run tests across multiple browsers (e.g., Chrome, Firefox, Edge, Safari) to validate cross-browser compatibility and identify potential issues.
- **Enable Continuous Testing:** Integrate with continuous integration (CI) tools to run tests automatically, ensuring that new changes do not introduce regressions or break existing functionality.

By achieving these objectives, this project aims to create a robust, maintainable, and scalable test automation framework for the HRM platform.


## Test Suite:

### Test Case-1:
1. Create an Excel file which will comprise of following as given below:
2. Using Data Driven Testing Framework (DDTF) you verify whether the login is successful or not for given usernames and passwords. After successful login, logout from the CRM.
3. Using cookies only verify whether login is successful or not

### Test-Case-2:
1. Verify whether the home URL is working or not?

### Test-Case-3:
1. Verify whether the username, password input boxes are visible or not.

### Test-Case-4:
1. Verify after successful login, whether the Menus 
   1. Admin, 
   2. PIM, 
   3. Leave, 
   4. Time, 
   5. Recruitment, 
   6. My Info, 
   7. Performance, 
   8. Dashboard are visible or not?

2. Verify after successful login, whether the Menus 
   1. Admin, 
   2. PIM, 
   3. Leave, 
   4. Time, 
   5. Recruitment, 
   6. My Info, 
   7. Performance, 
   8. Dashboard are clickable or not?

### Test-Case-5:
1. Create new user, 
2. Verify whether the new user is able to log-in into the CRM or not?


### Test-Case-6:
1. Verify from the Admin Menu that the new user exists in the records of the user or not?

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [License](#license)


## Features

- **Page Object Model (POM):** Separation of test logic and UI interactions. Each web page has its own corresponding class that defines methods for interacting with the elements on that page.
- **Pytest Framework:** Used to manage test cases, execute tests, and generate detailed reports.
- **Reusable Components:** Common actions like login, navigating to sections, and performing shutdown operations are encapsulated in reusable methods, improving maintainability.
- **Cross-Platform Compatibility:** The framework can be run across different environments, supporting different operating systems and web browsers.
- **Automation and Reporting:** Automation of repetitive tests with detailed reports on test results, making it easier to monitor and debug test executions.


## Tech Stack

- **Programming Language**: Python
- **Test Framework**: pytest and DDTF
- **Automation Tool**: Selenium WebDriver
- **Reporting**: pytest-html
- **Browser Compatibility**: Microsoft Edge, Google Chrome, Mozilla Firefox, Safari
- **CI/CD Integration**: GitHub Actions


## Setup and Installation

To set up and run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/imranc07/Mini_Project_2.git
   cd Mini_Project_2
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory to store sensitive information such as login credentials and URLs. Example:
     ```
     BASE_URL=https://example.com
     USER_EMAIL=test@example.com
     USER_PASSWORD=yourpassword
     ```

## Running Tests

To execute tests, use the following commands:

1. **Run All Tests**:
   ```bash
   pytest
   ```

2. **Generate HTML Report**:
   ```bash
   pytest --html=Reports/test_report.html
   ```

3. **Run Tests by Marker** (e.g., only "login" tests):
   ```bash
   pytest TestScripts/test_HomePage.py::test_home_url
   ```

4. **Headless Browser Execution**:
   - You can set up tests to run in Headless mode directly in your test script.

---

## Project Structure:
```
Mini_Project_2/
│
├── PageObjects/             # Contains Page Object Models HRM Web applications
│   ├── HomePage.py          # Handles methods and elements for HomePage
│   ├── PimPage.py           # Handles methods and elements for PimPage
│
├── Reports/                 # Contains HTML reports
│   ├── test_report.html     # HTML reports generated by pytest
│   
├── TestData/                # Stores test data for the test cases
│   ├── data.py              # Contains reusable test data
│   ├── testdata.xlx         # Contains reusable test data and test log
│
├── TestLocators/            # Stores locators for web elements
│   ├── locators.py          # Contains locators for all web elements used in the tests
│
├── TestScripts/             # Contains all test cases
│   ├── test_HomePage.py     # Test cases for HRM HomePage
│   ├── test_LoginPage.py    # Test script for data-driven login functionality
│   ├── test_PimPage.py      # Test cases for HRM PimPage
│
├── Utilities/               # Contains utility files
│   ├── excel_functions.py   # Script with functions for handling and testing Excel operations
│
├── requirements.txt         # Lists project dependencies
│
└── README.md                # Project documentation
```

---

## License
This project is open-source and available under the **"MIT License"**.

    ```
    Feel free to adjust the content based on your specific project setup!
    ```
    
