Feature: testing around the wikidex website

    Scenario Outline: last normal-type move
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that the last normal-type move that learns by leveling-up is <move>
    
    Examples: Pokemons
        |pokemon|move|
        |Gliscor|Danza espada|
        |Piplup|Ataque furia|
        |Smoliv|Pulso de campo|