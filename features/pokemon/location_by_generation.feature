@pokemon
Feature: Wikidex - Location by generation

    Scenario Outline: Assert one of the possible locations for some Pokemon in specific games
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that its location in the game <game> is <location>

    Examples: Pokemons
        |pokemon|game|location|
        |Pikachu|Escudo|Ruta 4|
        |Starly|Arceus|Pradera Obsidiana|
        |Croagunk|Negro 2|Ruta 8|