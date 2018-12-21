# ALPHA
A simple Django ToDO list applictaion

A ToDo list application is a list of errands and other tasks, that one needs or intends to accomplish.</br>


# Prerequisites
-[Python3](https://www.python.org/) (A programming language).<br>
-[Django](https://www.djangoproject.com/) (A high-level Python Web framework).<br>
-[PostgreSQL](http://www.postgresqltutorial.com/) (Database).<br>
-[Virtualenv](https://virtualenv.pypa.io/en/latest/) (Stores all dependencies used in the project).<br>
-[Pivotal Tracker](https://www.pivotaltracker.com/dashboard) (A project management tool).<br>

# Endpoints/
Method | EndPoint | Description | 
-------|----------|---------------|
POST| /todolist/users | User Regisration|
POST| /todolist/login | Login signed up user|
POST| /todolist/lists | Create a list of items|
GET| /todolist/lists | Fetch all items that are Created | 
GET| /todolist/list/int:listId | Fetch a single record|
PUT| /todolist/list/int:listId | Modify a Record|
DELETE| /todolist/list/int:listId | Delete a Record|


# Installation
Clone this Repository.
```
    $ git clone https://github.com/Ruiru11/ALPHA.git 
```
Create the virtual Environment
```
    $ virtualenv venv
```
Activate the virtual environment
```
    $ . venv/bin/activate
```
Install all the requirements
```
    $ pip install -r requirements.txt
```

# Create a .env file and add the following llines.
Configure with a preffered DB_NAME and DB_USER

export DATABASE_NAME="database"<br>
export DATABASE_USER ="postgres"<br>
export DATABASE_PASSWORD=""

Run the App<br>
    `python3 manage.py`

Test the application<br>
    `python3 manage.py test`