Feature: Date Input component
	Where the user can change the number of months to achieve the the total amount that he'd like to save

	Background: 
		Given the user is on the saving goal page
    
	@manual
	Scenario Outline: User selects a future month
		Given the month on "reach goal by" component is the current month
		When the user selects the next month by "<clicking method>"
		Then the next month should be displayed

		Examples:
		| clicking method                          |
		| clicking on the chevron-right            |
		| clicking on the right keyboard arrow key |

	@manual
	Scenario Outline: User selects a past month
		Given the month on "reach goal by" component is the next month
		When the user selects the past month by "<clicking method>"
		Then the current month should be displayed

		Examples:
		| clicking method                         |
		| clicking on the chevron-left            |
		| clicking on the left keyboard arrow key |

	@manual
	Scenario Outline: User selects a past month from the current month
		Given the month on "reach goal by" component is the current month
		When the user selects the past month by "<clicking method>"
		Then the past month should not be displayed

		Examples:
		| clicking method                         |
		| clicking on the chevron-left            |
		| clicking on the left keyboard arrow key |