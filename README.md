Sure! Here's an updated README with instructions on how to run tests using Behave tags:

---

# Saving Goal Automation Project

This project contains automated tests for the Saving Goal page of a web application. The tests are written using the Behave framework and Selenium WebDriver.

## Project Structure

- **features/**: This directory contains the feature files which describe the test scenarios in Gherkin syntax.
  - **confirm_button.feature**: Tests related to the confirm button functionality.
  - **money_input_component.feature**: Tests for the money input component where users can input their savings goal.
  - **monthly_amount_component.feature**: Tests for the monthly amount component that calculates monthly savings.
- **steps/**: This directory contains the step definitions for the feature files.
  - **confirm_button_steps.py**: Step definitions for the confirm button feature.
  - **money_input_steps.py**: Step definitions for the money input component feature.
  - **monthly_amount_steps.py**: Step definitions for the monthly amount component feature.
- **environment.py**: This file contains setup and teardown hooks for the test environment.

## Feature Files

### Confirm Button

**Feature: Confirm Button**  
Where the user can see and try to interact with the button that would confirm his saving goal.

#### Scenarios

- **Check if Confirm button is visible on the screen**
  - The confirm button should be visible on the screen.

- **No action by clicking on Confirm button**
  - When the user clicks on the confirm button, nothing should happen.

### Money Input Component

**Feature: Money Input Component**  
Where the user can insert the total amount that they'd like to save.

#### Scenarios

- **User can input only numbers in the total amount field**
  - The input should be rejected and not appear in the field when non-numeric characters are entered.

- **User can input valid money amount in the total amount field**
  - The input should be formatted as money and appear correctly in the field.

- **User can edit existing input in the total amount field**
  - The new input should be formatted as money and appear correctly in the field.

### Monthly Amount Component

**Feature: Monthly Amount Component**  
Where the user can see how much they should save per month to achieve their goal.

#### Scenarios

- **Check monthly value according to month**
  - The monthly amount should be calculated correctly based on the total amount and the selected month.

## Step Definitions

The step definitions for the test scenarios are implemented in Python using the Behave framework and Selenium WebDriver. Here are the key steps:

### Confirm Button Steps

- Navigate to the saving goal page.
- Check the visibility of the confirm button.
- Handle the click action on the confirm button and verify no redirection occurs.

### Money Input Steps

- Handle user input in the total amount field.
- Validate that only numeric inputs are accepted and formatted correctly as money.
- Allow editing of the existing input and ensure the new value is formatted correctly.

### Monthly Amount Steps

- Set the value in the total amount field.
- Change the month in the "reach goal by" component and verify the monthly amount is calculated correctly.

## Environment Setup

The `environment.py` file contains the setup and teardown methods for the test environment.

- **before_all(context)**: Initializes the WebDriver instance.
- **after_all(context)**: Quits the WebDriver instance after all tests are run.

## Running the Tests

To run the tests, execute the following command in the project root directory:

```bash
behave
```

### Running Specific Scenarios with Tags

You can use tags to run specific scenarios. Tags are defined in the feature files with the `@` symbol. For example, to run all scenarios tagged with `@automated`, use the following command:

```bash
behave --tags=@automated
```

You can also combine tags to include or exclude certain scenarios:

- **Run scenarios with multiple tags**:

  ```bash
  behave --tags=@tag1 --tags=@tag2
  ```

- **Run scenarios with either of the tags**:

  ```bash
  behave --tags=@tag1,@tag2
  ```

- **Exclude scenarios with a tag**:

  ```bash
  behave --tags=~@tag1
  ```

Ensure you have the required dependencies installed and the WebDriver executable in your PATH.

## Dependencies

- Behave
- Selenium

You can install the dependencies using pip:

```bash
pip install behave selenium
```

---

This README provides an overview of the project, its structure, features, and detailed instructions for running the tests, including using tags with Behave. If you have any additional details or specific requirements, please let me know!