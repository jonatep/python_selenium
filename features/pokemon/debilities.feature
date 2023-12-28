@test
Feature: Wikidex - Test debilities of Pokemon

    Scenario Outline: Check debilities por certain Pokemon
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that its debilities are <debilities>

    Examples: Pokemons
        |pokemon|debilities|
        |Tyranitar|Lucha, Acero, Agua, Bicho, Hada, Planta, Tierra|
        |Delibird|Roca, Acero, Eléctrico, Fuego|
        |Snorlax|Lucha|