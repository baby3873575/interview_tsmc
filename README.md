## Problem statement
Topic: Query and display user’s ToDo, Post and Comment information. 

User master data:
https://jsonplaceholder.typicode.com/users

 

User related data subjects
https://jsonplaceholder.typicode.com/todos

https://jsonplaceholder.typicode.com/posts

https://jsonplaceholder.typicode.com/comments

 
User scenario includes:
1. The home page show all user’s basic information
2. Choose one or many user then show up his or their ToDo, Post and Comment fields.
 

The work includes backend server and frontend web application.

1. The backend query data source and aggregate data by user id.
2. The backend expose API for web query user information.
3. The frontend web display user information and aggregated ToDo, Post and Comment.
 

#### Check points:
1. Performance excellent
2. User experience
3. Code structure
4. Unit test


## Development Guide
### Prerequisite
1. docker, docker-compose
2. python 3.8
3. node v14.15.1

### Steps
1. Runs an mongodb with docker-compose
```
docker-compose up -d
```

2. Start Backend with development server

It's better to have a virtualenv to seperate python packages
```
virtualenv venv
source venv/bin/activate
```
Install the dependencies:
```
pip install -r requirements.txt
```
Run the development webserver:
```
python api/manage.py runserver
```

Now the application server should be up and running so we can access: http://localhost:5000/apidocs/
Please help to trigger sync_users by invoke /api/v1/usersync. Feel free to use the swagger UI to fire a request to POST /api/v1/usersync.
After the usersync is invoked, server will request data source and save the data to storage for other APIs to utilize.

3. Starts Front End dev server

Please help to open another terminal as we still need backend server running.
```
cd ui/
npm install
npm run start
```

4. Finally, you should be able to see the UI and integrated with backend 



### Unit testing

For backend:
```
cd api
pytest 
```
For frontend:
```
cd ui
npm run test
```


## Memo
1. Time limit: 2days
2. Should have put frontend and backend into docker-compose 
