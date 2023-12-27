Feature: Testing around Amazon's website
    
    Scenario Outline: changing image when hovering
        Given I go to an Amazon <product>
        Then I can assert that, when hovering over variations of the product, the image changes

    Examples: Products
        |product|
        |https://www.amazon.com/-/es/TAMASHII-NATIONS-Jujutsu-Kugisaki-S-H-Figuarts/dp/B08MGHWFS1?ref_=Oct_DLandingS_D_4700f620_7&th=1|
        |https://www.amazon.com/Amazon-Essentials-Pantuflas-mocas%C3%ADn-hombre/dp/B09RXJD1S4/ref=sr_1_1_ffob_sspa?crid=38K9E58R8ZS0R&keywords=slippers&qid=1703601645&sprefix=%2Caps%2C371&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1|

    Scenario Outline: checking discount
        Given I go to an Amazon <product>
        Then I can assert that the product shows an accurate discount percent in its price

    Examples: Products
        |product|
        |https://www.amazon.com/-/es/Legend-Zelda-Kingdom-videojuego-Nintendo-Version/dp/B097B2YWFX/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1|
        |https://www.amazon.com/ornitorrinco-adultos-cosplay-Navidad-Halloween/dp/B0CCXTMMHM/ref=sr_1_1_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2PZBFHAG4WXW8&keywords=perry%2Bthe%2Bplatypus%2Bpijama&qid=1703605078&sprefix=perry%2Bthe%2Bplatypus%2Bpijama%2Caps%2C204&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1|

    Scenario Outline: checking box coupon
        Given I go to an Amazon <product>
        Then If I click on the coupon checkbox, I go to the login page
        When I go to the previous tab
        Then I can assert that the coupon checkbox is not selected

    Examples: Products
        |product|
        |https://www.amazon.com/dp/B08CXWDBTY/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pd_rd_plhdr=t&aref=4B44B8F3EF885D505B66FC6D3C5497CC359B22889BAE304C9DD23456668799F3|
    
    @test
    Scenario Outline: changing currency
        Given I have opened Amazon
        When I select the currency <currency> in the currency dropdown
        Then The products are displayed with the currency <currency>

    Examples: Currencies
        |currency|
        |EUR| 
        |JPY| 
        |MUR| 
    