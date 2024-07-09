Feature: Confirm Button
  Where the user can see and try to interact with the button that would confirm his saving goal

  Background:
    Given the user is on the saving goal page

  @automated
  Scenario: Check if Confirm button is visible on the screen
    Then the confirm button should be visible on the screen

  @automated
  Scenario: No action by clicking on Confirm button
    When the user clicks on the confirm button
    Then nothing should happen