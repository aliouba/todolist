# Stack

This API Service is built in Django 2.1, Python 3.7.0 and Postgres 10.4.

# Deployment: the easy way  

To deploy easily, the dockerfile docker-compose files were generated. 

1. Install Docker (https://docs.docker.com/install/) and Docker Compose (https://docs.docker.com/compose/install/)

2. Clone this repository: git clone https://github.com/aliouba/todolist

3. Deploy with "docker-compose up" commmand. The API Service port exposed is 8000.

4. Populate Postgres Database: docker exec -it todolist_web_1 python3 manage.py migrate

5. Create super Admin User: docker exec -it todolist_web_1 python3 manage.py createsuperuser

6. You can create additinal users via django admin console (/admin/)

## API ENDPOINTS

# Login 

URL: /rest-auth/login/

METHOD: POST 

HEADER: Content-Type:application/json

DATA: {"password": "<password>","username": "<username>"}

Response: {"key": "<Your Token>"}
  
Response Code:  200

# Logout

URL: /rest-auth/logout/

METHOD: POST 

HEADER: Content-Type:application/json, Authorization: Token + <Your Token>

Response: { "detail": "Successfully logged out."}

Response Code:  200

# Create a new todo item

URL: /todolist/

METHOD: POST 

HEADER: Content-Type:application/json, Authorization: Token + <Your Token>

Data: {"name": "My todo item name","description": "My todo item Description"}

Response: {
    "id": <item ID>,
    "name": "My todo item name",
    "description": "todo item Description",
    "useruid": <User ID that created this item>,
    "completed": false
}

Response Code:  201

# List user's set of todo items (All items of authenticated user)

URL: /todolist/

METHOD: GET 

HEADER: Content-Type:application/json, Authorization: Token + <Your Token>

Response: [
    {
    "id": <item ID>,
    "name": "My todo item name",
    "description": "todo item Description",
    "useruid": <User ID that created this item>,
    "completed": false
    },
      {
    "id": <item ID>,
    "name": "My todo item name",
    "description": "todo item Description",
    "useruid": <User ID that created this item>,
    "completed": false
    }...
]

Response Code:  200

# Get a single todo item

URL: /todolist/<item ID>/

METHOD: GET 

HEADER: Content-Type:application/json, Authorization: Token + <Your Token>

Response: {
    "id": <item ID>,
    "name": "My todo item name",
    "description": "todo item Description",
    "useruid": <User ID that created this item>,
    "completed": false
    }

Response Code:  200

# Modify a single todo iem (eg mark it as completed)

URL: /todolist/<item ID>/

METHOD: PUT 

HEADER: Content-Type:application/json, Authorization: Token + <Your Token>

Data: {"completed": 1}

Response: {
    "id": <item ID>,
    "name": "My todo item name",
    "description": "todo item Description",
    "useruid": <User ID that created this item>,
    "completed": True
}

Response Code:  200

# Delete a todo item

URL: /todolist/<item ID>/

METHOD: DELETE 

HEADER: Content-Type:application/json, Authorization: Token + <Your Token>

Response: EMPTY

Response Code:  204
