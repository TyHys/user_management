# Developer Notebook:
* Composed the docker image and navigated to PGAdmin, got Postgres setup per instructions. No issues.
* Ran the Alembic migration script to load the tables/schemas in Postgres, no issues.
* Navigated to http://localhost/docs & registered a new user successfully.
    * It took me a long time to realize the admin authentication method from Homework 10 no longer worked and I burned a few days here before asking others in the Discord.
    * After this I realized that I needed to begin by registering a user when I have no authentication.
* Authenticated the user via the email being the 'user id' (I'm not proud of how long it took me to realize that the user ID was the email and not the UUID).
* Executed the Get User endpoint successfully, returned the correct data.
* Spent several days (intermitently) trying to figure out why an email was not received in MailTrap.
    * Realized that an email isn't sent for the initial admin user. (ouch)
* Registered a second user, successfully received email into MailTrap.
* Link didn't appear to be valid. Modified the user_service.py to correct for invalid token in link.
* Clicked the link within the email, and logged in successfully.
* Queried the users table & saw that the email_verified bool was flipped to TRUE for the user.
* Admin user was changed to authenticated in Postgres
* Added check to see that user is ANONYMOUS in user_service.py as well.
* Noticed that registering a user doesn't actually show you the full details in the response body.
* Modified the response model in user_management/app/routers/user_routes.py to correct for this.
* Noticed a similar issue in the response model for the /myaccount endpoint.
    * Corrected this, similar to the preivous issue.
* Added a route to change the professional status of an account.
* Added an email template and successfully tested the automatic sending.
* Wrote new tests for the additional endpoint

⫸ 
⪢
⪼
⪫
