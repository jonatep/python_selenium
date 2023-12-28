@test
Feature: Changing image when hovering
    
    Scenario Outline: Check that the main image of a product changes when the cursor is hovering over its variations
        Given I go to an Amazon <product>
        Then I can assert that, when hovering over variations of the product, the image changes

    Examples: Products
        |product|
        |https://www.amazon.com/-/es/TAMASHII-NATIONS-Jujutsu-Kugisaki-S-H-Figuarts/dp/B08MGHWFS1?ref_=Oct_DLandingS_D_4700f620_7&th=1|
        |https://www.amazon.com/Amazon-Essentials-Pantuflas-mocas%C3%ADn-hombre/dp/B09RXJD1S4/ref=sr_1_1_ffob_sspa?crid=38K9E58R8ZS0R&keywords=slippers&qid=1703601645&sprefix=%2Caps%2C371&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1|