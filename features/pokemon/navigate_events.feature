@test
Feature: Wikidex - Navigate to events

    Scenario Outline: Navigation through menus to access specific events on an specific year 
        Given I have opened the wikidex website
        When I navigate to Pokemon GO and click on the events from <year>
        Then I can assert that the event <event> started on <date>

    Examples: Events
        |event|year|date|
        |Semana de la moda|2023|15 de octubre del 2023|
        |Halloween|2016|20 de octubre del 2017|
        |Golden Week|2017|29 de abril del 2017|
        |Ultrabonus|2021|23 de julio del 2021|

