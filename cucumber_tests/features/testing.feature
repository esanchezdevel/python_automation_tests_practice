Feature:

    Scenario: Login to caratlane with valid parameters
        Given Launching chrome BaseBrowser
        When Open caratlane Login page
        And Enter username "XXXXX.com"
        And click continue to login button
        And Enter Password "YYYYYYY"
        #And click on the Login Button
        #Then User must logined successfully