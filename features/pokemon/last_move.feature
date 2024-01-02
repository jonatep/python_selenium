@pokemon
Feature: Wikidex - Checking last moves

    Scenario Outline: Assert the last move learned by an specific Pokemon, in an specific game and of an specific type
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that the last <attack_type>-type move that learns by leveling-up in the game <game> is <move>
    
    Examples: Pokemons
        |pokemon|move|game|attack_type|
        |Snorunt|Triturar|3ª gen|siniestro|
        |Gliscor|Danza espada|Escarlata y Púrpura|normal|
        |Piplup|Ataque furia|Escarlata y Púrpura|normal|
        |Smoliv|Pulso de campo|Escarlata y Púrpura|normal|
        |Togepi|Fuerza lunar|Arceus|hada|