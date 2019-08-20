
# Python Selenium Behave Page-Object-Model(POM) Docker
Run your Selenium BDD test cases in Docker. Python, Selenium, Behave, Chrome, Docker.


# Demo
**`Behave`** is Python-Selenium equivalent of **`Cucumber`** Ruby-Capybara. You can run your BBD test cases in the same 
way with some little differences. See the demo which runs Behave in Docker:
![Behave demo GIF](img/behave.gif)

# Running a Feature on Docker
```bash
~/P/p/m/web-automation (master ⚡☡=) docker run --network host --rm --name behave -v $PWD:/project gunesmes/python-selenium-behave-page-object-docker bash -c "export BROWSER=iphone6 && behave features/M001-users_checking.feaure"
GNU/Linux
Feature: Checking users # features/M001-users_checking.feature:1

  Background: go to the main page of the app  # features/M001-users_checking.feature:3

  @user_check @smoke
  Scenario: Users page feature      # features/M001-users_checking.feature:7
    Given I open the web app        # features/steps/map_users_create.py:10
    When I should see created users # features/steps/map_users_create.py:80



1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
2 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.785s
```

# Running UI Test on CI
For CI, whole tests can be by run `bash run_web_automation.sh`. Each tags run for each platforms in different docker 
instance. Therefore for this demo, there 12 docker instance runs the test cases. `20 test casea` took `34 seconds` to finish. See the logs: 

* Tags: `create`, `create_check`, `user_check`
* Platforms: `desktop` `iphone6` `iphoneX` `pixel2` 

```bash
~/P/p/m/web-automation (master ⚡☡=) bash run_web_automation.sh
 - Get the latest docker images
latest: Pulling from gunesmes/python-selenium-behave-page-object-docker
Digest: sha256:4a7a571911bc53b902e7a904ee9653d6738c527f9d74d32df76703c8c8c323db
Status: Image is up to date for gunesmes/python-selenium-behave-page-object-docker:latest

 - Test running on
    https://localhost:8001


 - Running tests: create on desktop
 - Running tests: create on iphone6
 - Running tests: create on iphoneX
 - Running tests: create on pixel2
 - Running tests: create_check on desktop
 - Running tests: create_check on iphone6
 - Running tests: create_check on iphoneX
 - Running tests: create_check on pixel2
 - Running tests: user_check on desktop
 - Running tests: user_check on iphone6
 - Running tests: user_check on iphoneX
 - Running tests: user_check on pixel2

 - - - - - -  RESULT  - - - - - - -


1 feature passed, 0 failed, 1 skipped
1 scenario passed, 0 failed, 4 skipped
2 steps passed, 0 failed, 31 skipped, 0 undefined
Took 0m2.266s


1 feature passed, 0 failed, 1 skipped
1 scenario passed, 0 failed, 4 skipped
2 steps passed, 0 failed, 31 skipped, 0 undefined
Took 0m2.457s


1 feature passed, 0 failed, 1 skipped
1 scenario passed, 0 failed, 4 skipped
2 steps passed, 0 failed, 31 skipped, 0 undefined
Took 0m2.526s


1 feature passed, 0 failed, 1 skipped
1 scenario passed, 0 failed, 4 skipped
2 steps passed, 0 failed, 31 skipped, 0 undefined
Took 0m2.488s


1 feature passed, 0 failed, 1 skipped
3 scenarios passed, 0 failed, 2 skipped
27 steps passed, 0 failed, 6 skipped, 0 undefined
Took 0m18.186s


Failing scenarios:
  features/M002-register.feature:29  User creation feature -- @1.1 User data

0 features passed, 1 failed, 1 skipped
2 scenarios passed, 1 failed, 2 skipped
26 steps passed, 1 failed, 6 skipped, 0 undefined
Took 0m17.771s


Failing scenarios:
  features/M002-register.feature:29  User creation feature -- @1.1 User data

0 features passed, 1 failed, 1 skipped
2 scenarios passed, 1 failed, 2 skipped
26 steps passed, 1 failed, 6 skipped, 0 undefined
Took 0m19.375s


Failing scenarios:
  features/M002-register.feature:29  User creation feature -- @1.1 User data

0 features passed, 1 failed, 1 skipped
2 scenarios passed, 1 failed, 2 skipped
26 steps passed, 1 failed, 6 skipped, 0 undefined
Took 0m17.153s


1 feature passed, 0 failed, 1 skipped
1 scenario passed, 0 failed, 4 skipped
4 steps passed, 0 failed, 29 skipped, 0 undefined
Took 0m23.237s


1 feature passed, 0 failed, 1 skipped
1 scenario passed, 0 failed, 4 skipped
4 steps passed, 0 failed, 29 skipped, 0 undefined
Took 0m23.403s


1 feature passed, 0 failed, 1 skipped
1 scenario passed, 0 failed, 4 skipped
4 steps passed, 0 failed, 29 skipped, 0 undefined
Took 0m23.362s


1 feature passed, 0 failed, 1 skipped
1 scenario passed, 0 failed, 4 skipped
4 steps passed, 0 failed, 29 skipped, 0 undefined
Took 0m23.836s

 - All processes done!
 - 0 minutes and 34 seconds elapsed.
``` 

# Reporting with Allure Report
Allure report plug-in gives very good graphics and explanation. Integration is very easy check the related Jenkins image.
![Allure Report](screencapture-localhost-8080-job-UITest-allure-2019-08-20-14_51_36.png) 
