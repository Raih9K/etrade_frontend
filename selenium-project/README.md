# Selenium Project

This project is a structured Selenium automation framework designed for testing a web application. It utilizes the Page Object Model (POM) to organize locators and page interactions, making the tests more maintainable and readable.

## Project Structure

- **locators/**: Contains files that define locators for different pages.
  - `landing_page_locators.py`: Locators for the landing page.
  - `account_login_page_locators.py`: Locators for the account login page.
  - `cart_page_locators.py`: Locators for the cart page.
  - `checkout_page_locators.py`: Locators for the checkout page.
  - `profile_page_locators.py`: Locators for the profile page.

- **pages/**: Contains page classes that encapsulate interactions with the web application.
  - `landing_page.py`: Class for the landing page.
  - `account_login_page.py`: Class for the account login page.
  - `cart_page.py`: Class for the cart page.
  - `checkout_page.py`: Class for the checkout page.
  - `profile_page.py`: Class for the profile page.

- **tests/**: Contains test cases for each page.
  - `test_landing_page.py`: Tests for the landing page.
  - `test_account_login_page.py`: Tests for the account login page.
  - `test_cart_page.py`: Tests for the cart page.
  - `test_checkout_page.py`: Tests for the checkout page.
  - `test_profile_page.py`: Tests for the profile page.

- **conftest.py**: Configuration file for pytest, including fixtures for setting up and tearing down the Selenium WebDriver.

- **requirements.txt**: Lists the dependencies required for the project, such as `pytest`, `selenium`, and any other necessary libraries.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd selenium-project
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the tests**:
   ```
   pytest tests/
   ```

## Usage

- Each test file in the `tests` directory corresponds to a specific page and contains test cases that utilize the methods defined in the respective page classes.
- The locators for each page are defined in the `locators` directory, allowing for easy updates and maintenance.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.