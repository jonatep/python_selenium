@test
@amazon
Feature: Changing currency
    
    Scenario Outline: Try to change the Amazon currency, and check that it has been applied
        Given I have opened Amazon
        When I select the currency <currency> in the currency dropdown
        Then The products are displayed with the currency <currency>

    Examples: Currencies
        |currency|
        |EUR| 
        |JPY| 
        |MUR| 
    