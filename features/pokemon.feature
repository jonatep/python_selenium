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

    Scenario Outline: location by generation
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that its location in the game <game> is <location>

    Examples: Pokemons
        |pokemon|game|location|
        |Pikachu|Escudo|Ruta 4|
        |Starly|Arceus|Pradera Obsidiana|
        |Croagunk|Negro 2|Ruta 8|