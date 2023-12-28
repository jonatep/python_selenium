@test
Feature: Wikidex - Checking levels of evolution

    Scenario Outline: Assert the levels and/or methods by which some Pokemon can evolve
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that its levels of evolution are <levels>

    Examples: Pokemons
        |pokemon|levels|
        |Bidoof|Nivel 15|
        |Poliwag|Nivel 25, Piedra agua, Intercambio equipado con roca del rey|