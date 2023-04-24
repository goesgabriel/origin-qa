Feature: Monthly amount component
  Where the user can see how much he should save by month to achieve his goal

  Background:
    Given the user is on the saving goal page

  @automated
  Scenario Outline: Check monthly value according with month
    Given the "total amount" field value is "<total amount equal to>"
    When the month on "reach goal by" component is the "<month>"
    Then the "monthly amount" field value is "<monthly amount equal to>"

    Examples:
      | total amount equal to | month         | monthly amount equal to |
      | 1,000.00              | current month | 1,000.00                |
      | 1,000.00              | next month    | 500.00                  |
      | 1,000.00              | next month +2 | 250.00                  |
