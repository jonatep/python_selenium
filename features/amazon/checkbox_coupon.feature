@test
Feature: Checking box coupon
    
    Scenario Outline: When clicking on a coupon from an Amazon product, then going back to its page, check if the checkbox is disabled
        Given I go to an Amazon <product>
        Then If I click on the coupon checkbox, I go to the login page
        When I go to the previous tab
        Then I can assert that the coupon checkbox is not selected

    Examples: Products
        |product|
        |https://www.amazon.com/dp/B08CXWDBTY/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pd_rd_plhdr=t&aref=4B44B8F3EF885D505B66FC6D3C5497CC359B22889BAE304C9DD23456668799F3|