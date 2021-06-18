# OPM Consultant Database

## Setup
Clone the repo, set up a virtual environment and install requirements, then from a command line in the project root folder do: ```python manage.py migrate``` to run database migrations. Make sure to set up the database locally and update ```settings.py``` before running migrations. Finally do ```python manage.py runserver``` to start a development server.

## Database
This uses postgres by default. You will need the postgres service running locally, and update ```settings.py``` to configure. 

## Deployment
This is mostly configured to deploy using Dokku out of the box. Once you have Dokku running on the server, you should just be able to ```git push``` to get the site deployed.
