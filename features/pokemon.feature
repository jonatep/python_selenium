Feature: testing around the wikidex website

    Scenario Outline: last specific-type move by game
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

