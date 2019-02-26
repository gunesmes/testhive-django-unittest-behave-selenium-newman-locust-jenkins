Feature: Checking users

  Background: go to the main page of the app 
    Given I open the web app          

	  @user_check @smoke
	  Scenario: Users page feature     
	    When I should see created users

	  @user_check
	  Scenario: Users page feature
	  	When I click "testusername1" on users page
	  	Then I should see the detail of "testusername1"
