Feature: Checking discount
    
    Scenario Outline: Check that the shown discount percent in an Amazon product is accurate with its actual price
        Given I go to an Amazon <product>
        Then I can assert that the product shows an accurate discount percent in its price

    Examples: Products
        |product|
        |https://www.amazon.com/Super-Mario-World-Bowsers-Fury/dp/B08JCZKTQW/ref=sr_1_5?crid=OF2SCSH1NY8H&keywords=switch+games&qid=1703682273&sprefix=switch+game%2Caps%2C178&sr=8-5|
        |https://www.amazon.com/ornitorrinco-adultos-cosplay-Navidad-Halloween/dp/B0CCXTMMHM/ref=sr_1_1_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2PZBFHAG4WXW8&keywords=perry%2Bthe%2Bplatypus%2Bpijama&qid=1703605078&sprefix=perry%2Bthe%2Bplatypus%2Bpijama%2Caps%2C204&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1|
