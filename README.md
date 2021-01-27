# naviaAssignment
Assignment as per requirement

## Requirements: python > 3.5

## How to run it:
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver


### How to use:
This will ensure a server running on port 8000.

Navigate to http://localhost:8000/medicine/

- You can either import the data into DB using import file option or search a medicine in inventory and get it's details.
- Allowes searches: Exact name of medicine, Partial name of medicine that starts with given text.


## Implementation:
- DB used: sqlite3
- Number of tables = 1, as there is 1-1 relationship b/w every element. For duplicates their salt name/dosage and few other components were different. 
- Search implementation is done via simple db query considering the size of data.
- Autosuggest is not implemented as it was not required in the assignment but can be done via simple db query.
- Import: Import is currently a time taking query as it's synchronous as of now.

# How to Scale:
- sqlite3 can be replaced with mysql.
- Autosuggest:  To scale the autosearch, we might elasticsearch in which use another pipeline where MySQL event publisher triggers message into a queue (emqx/rabbitmq) and is consumed by logstash/consumer service to put in elasticsearch. (Why Elasticsearch ? - It provides option to tokenise the words to have fast query based searching, Challenges: Updating of existing data and removing of data from elasticsearch when data is removed from db (delete_by_query/update) )
- Import: Importing data can be switched to asynchronus by using background_task feature of django. This will reduce the user response time.
