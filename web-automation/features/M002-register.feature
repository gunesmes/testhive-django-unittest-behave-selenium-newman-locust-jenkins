Feature: Creating users

  Background: go to the register page of the app 
    Given I restore the database   
    And I open the web app          
    And I open the register page           

  @create_check @smoke
  Scenario: User creation form checks                                         
    Then I should ensure that all the empty fields give approprate warnings
      | username | email          | birthday    | address                         | warning                     |
      |          | test1@test.com | 2000-11-20  | Bredgatan 4 211 30 Malmö Sweden | Please fill out this field. |
      | test1    |                | 2000-11-20  | Bredgatan 4 211 30 Malmö Sweden | Please fill out this field. |
      | test1    | test1@test.com |             | Bredgatan 4 211 30 Malmö Sweden | Please fill out this field. |
      | test1    | test1@test.com | 2000-11-20  |                                 | Please fill out this field. |


  @create @smoke
  Scenario Outline: User creation feature     
    When I enter <username> for user name   
    And I enter <email> for e-mail          
    And I enter <birthday> for birthday     
    And I enter <address> for address       
    And I click on Register button        
    Then I should see the correct <message> 

    Examples: User data
      | username         | email             | birthday       | address                           | message                                     |
      | "testusername30" | "test30@test.com" | "03.03.2000"   | "Bredgatan 4 211 30 Malmö Sweden" | "User is recorded with given informations." |
      | "testusername1"  | "test1@test.com"  | "03.04.2010"   | "Bredgatan 4 211 30 Malmö Sweden" | "Users with this Username already exists."  |
      | "testusername33" | "test1@test.com"  | "10.10.200002" | "Bredgatan 4 211 30 Malmö Sweden" | "Enter a valid date."                       |