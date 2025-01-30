# Hello
### This template is a CRUD project implemented with FastAPI and SQLMODEL

In this project you will see an `app` folder and an `alembic` folder
You can also view a `requirments.txt` file that is all the packages needed to execute and test this project within this file.

## Well, let's go to your guidance to descripyion this project.
after open the `app` directory you can see 4 another directory that them are Core of project

also we have `config.py` in the app directory that all setting are in this file.
and you can see `database.py` file that, as its name implies, relates to the database connection to our project
And the most important file in this folder is the `main.py` file that is to run the project by Fasapi
also we have `dependencies.py` that we give session of our database.
You also see an `auth.py` file that is not yet completed and the user access logic will be implemented to build updates and read data in this file and be used in different sections of the project.

# models
### in models directory we create models(tablse) by SQLModel and make relations with another models
we have `link` directory here that we create a "many-to-many" models --> **BookAuthorLink model**

# router
### in this directory we create a router that link to model services in `services` directory
In this folder we have defined the data structure in API requests and responses separately for each model and validated the columns of each model if needed

# services
### In the architecture of a Fastapi project, services are used as a layer of routers to manage business logic and communication with databases or other external resources. This separation enhances readability, testability, and code expansion. And we've done it
