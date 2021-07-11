Feature: Search Haircut Saloon

  Background: Opening the Consumers home page



  Scenario: Searching for haircut saloon with at least 3 search results
    Given The user has landed on consumers page
    And sees the consumer page elements
    And The user enters "haircut" in query field on consumer default search tile
    And user selects item# "1" in query dropdown on consumer default search tile
    And user enters "San" in location field on consumer default search tile
    And user selects item# "5" in location dropdown on consumer default search tile
    When user clicks on Search on consumer default search tile
    Then user lands on the search results page
    And user sees "3" search results on search results page

  Scenario: Open business with name "Test - Sabre Cuts"
    Given User is on search results page for "haircut" and "San Francisco, CA"
    And user clicks on the search result "Test - Sabre Cuts" on search result page
    And user sees express checkout page
    When user clicks on "All services" on services panel on express checkout page
    And user selects staff# "2" from staff filter on express checkout page
    And user clicks Book button for "Men's Haircut" service on express checkout page
    And user clicks selects time on add-on modal on express checkout page
    Then user lands on pick a time section on express checkout page
    And user sees the previously selected service, staff and price on time section on express checkout page