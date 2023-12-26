@test
Feature: Testing around Amazon's website
    
    Scenario Outline: changing image when hovering
        Given I have opened Amazon
        When I go to a <product>
        Then I can assert that, when hovering over variations of the product, the image changes

    Examples: Products
        |product|
        |https://www.amazon.com/-/es/TAMASHII-NATIONS-Jujutsu-Kugisaki-S-H-Figuarts/dp/B08MGHWFS1?ref_=Oct_DLandingS_D_4700f620_7&th=1|