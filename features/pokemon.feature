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

    Scenario Outline: egg moves
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that the egg moves that it can learn with <egg_pokemon> are <moves>

    Examples: Pokemons
        |pokemon|egg_pokemon|moves|
        |Dreepy|Yamask|Anulación, Maldición, Rabia|
        |Bidoof|Psyduck|Golpes furia, Hidrochorro|
        |Rowlet|Togetic|Relevo|

    Scenario Outline: levels of evolution
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that its levels of evolution are <levels>

    Examples: Pokemons
        |pokemon|levels|
        |Bidoof|Nivel 15|
        |Poliwag|Nivel 25, Piedra agua, Intercambio equipado con roca del rey|

    Scenario Outline: debilities
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that its debilities are <debilities>

    Examples: Pokemons
        |pokemon|debilities|
        |Tyranitar|Lucha, Acero, Agua, Bicho, Hada, Planta, Tierra|
        |Delibird|Roca, Acero, Eléctrico, Fuego|

    @test
    Scenario Outline: navigate to events 
        Given I have opened the wikidex website
        When I navigate to Pokemon GO and click on the events from <year>
        Then I can assert that the event <event> started on <date>

    Examples: Events
        |event|year|date|
        |Semana de la moda|2023|15 de octubre del 2023|
        |Halloween|2016|20 de octubre del 2017|
        |Golden Week|2017|29 de abril del 2017|
        |Ultrabonus|2021|23 de julio del 2021|

