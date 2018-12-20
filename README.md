# ALPHA
A simple Django ToDO list applictaion

A ToDo list aaplication is a list of errands and other tasks, that one needs or intends to accomplish.</br>


# Prerequisites
-[Python3](https://www.python.org/) (A programming language).<br>
-[Django](https://www.djangoproject.com/) (A high-level Python Web framework).<br>
-[PostgreSQL](http://www.postgresqltutorial.com/) (Database)
-[Virtualenv](https://virtualenv.pypa.io/en/latest/) (Stores all dependencies used in the project)<br>
-[Pivotal Tracker](https://www.pivotaltracker.com/dashboard) (A project management tool)<br>

# Endpoints/
EndPoint | Functionality | Notes
---------|---------------|-------
POST /todolist | Create a list of items|
GET /todolist | Fetch all items that are Created | 
GET /todolist/<listId> | Fetch a single record|
PUT /todolist | Modify a Record|
DELETE /todolist | Delete a Record|


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

export DATABASE_NAME="database"
export DATABASE_USER ="postgres"
export DATABASE_PASSWORD=""