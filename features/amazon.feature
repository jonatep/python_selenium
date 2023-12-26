Feature: Testing around Amazon's website
    
    Scenario Outline: changing image when hovering
        Given I have opened Amazon
        When I go to a <product>
        Then I can assert that, when hovering over variations of the product, the image changes