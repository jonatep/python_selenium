Feature: testing around the wikidex website

    Scenario Outline: last normal-type move
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that the last <attack_type>-type move that learns by leveling-up is <move>
    
    Examples: Pokemons
        |pokemon|move|attack_type|
        |Gliscor|Danza espada|normal|
        |Piplup|Ataque furia|normal|
        |Smoliv|Pulso de campo|normal|
        |Togepi|Fuerza lunar|hada|

    Scenario Outline: location by generation
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that its location in the game <game> is <location>

    Examples: Pokemons
        |pokemon|game|location|
        |Pikachu|Escudo|Ruta 4|
        |Starly|Arceus|Pradera Obsidiana|
        |Croagunk|Negro 2|Ruta 8|

    @test
    Scenario Outline: egg moves
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that the egg moves that it can learn with <egg_pokemon> are <moves>

    Examples: Pokemons
        |pokemon|egg_pokemon|moves|
        |Dreepy|Yamask|Anulación, Maldición, Rabia|
        |Bidoof|Psyduck|Golpes furia, Hidrochorro|