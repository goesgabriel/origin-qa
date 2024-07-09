Feature: Money Input component
  Where the user can insert the total amount that he'd like to save

  Background:
    Given the user is on the saving goal page

  @automated
  Scenario Outline: User can input only numbers in the total amount field
    When the user inputs "<non-numeric character>" in the total amount field using the keyboard
    Then the input should be rejected and not appear in the field

    Examples:
      | non-numeric character            |
      | abcdefghijklmnopqrstuvwxyz       |
      | ?:<>}^{`+_)(*&¨%$#@!",.;/]~[´=-\ |
      | °ºª§¹²³£¢¬                       |

  @automated
  Scenario Outline: User can input valid money amount in the total amount field
    When the user inputs "<valid money amount>" in the total amount field
    Then the value that should appear is "<formatted as money>"

    Examples:
      | valid money amount | formatted as money |
      | 100050             | 1,000.50           |

  @automated
  Scenario Outline: User can edit existing input in the total amount field
    Given the user inputs "<valid money amount>" in the total amount field
    When the user edits the total amount field value to "<new value>" using the keyboard
    Then the value that should appear is "<formatted as money>"

    Examples:
      | valid money amount | new value | formatted as money |
      | 100050             | 9876534   | 98,765.34          |