Feature: Wikidex - Checking egg moves

    Scenario Outline: Testing the egg moves of certain pokemon
        Given I have opened the wikidex website
        When I search for the Pokemon <pokemon>
        Then I can assert that the egg moves that it can learn with <egg_pokemon> are <moves>

    Examples: Pokemons
        |pokemon|egg_pokemon|moves|
        |Dreepy|Yamask|Anulación, Maldición, Rabia|
        |Bidoof|Psyduck|Golpes furia, Hidrochorro|
        |Rowlet|Togetic|Relevo|
