# Social Network API


## Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abhishekchalke/social_network.git
    cd social-network-api
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Use Docker to run the application**:
    ```bash
    docker-compose up --build
    ```




## Postman Collection

A Postman collection is provided to test the API endpoints easily.

1. **Import the collection into Postman**:
    - Open Postman.
    - Click on "Import" in the top left corner.
    - Select "Upload Files".
    - Choose the `social-network.postman_collection.json` file from the root directory of the project.
    - Click "Import".

2. **Use the requests in the collection to test the API**.




## Endpoints

### User Signup
- **URL**: `/users/api/signup/`
- **Method**: POST
- **Body**:
    ```json
    {
        "email": "user@example.com",
        "password": "password123"
    }
    ```



### User Login
- **URL**: `/users/api/login/`
- **Method**: POST
- **Body**:
    ```json
    {
        "email": "user@example.com",
        "password": "password123"
    }
    ```



### Send Friend Request
- **URL**: `/users/api/friend_request/reject/`
- **Method**: POST
- **Headers**: `Authorization: Token <user_token>`
- **Body**:
    ```json
    {
        "name": "friend_name"
    }
    ```



### Accept Friend Request
- **URL**: `/users/api/friend_request/reject/`
- **Method**: POST
- **Headers**: `Authorization: Token <user_token>`
- **Body**:
    ```json
    {
        "name": "friend_name"
    }
    ```



### Reject Friend Request
- **URL**: `/users/api/friend_request/reject/`
- **Method**: POST
- **Headers**: `Authorization: Token <user_token>`
- **Body**:
    ```json
    {
        "name": "friend_name"
    }
    ```


### List Friends
- **URL**: `/users/api/list/friends/`
- **Method**: POST
- **Headers**: `Authorization: Token <user_token>`



### List Friend Requests
- **URL**: `/users/api/list/friend_requests/`
- **Method**: POST
- **Headers**: `Authorization: Token <user_token>`



### Search Users
- **URL**: `/users/api/search/users/`
- **Method**: GET
- **Headers**: `Authorization: Token <user_token>`
- **Body**:
    ```json
    {
        "search":"search_name",
        "search_by":"name"
    }

    OR

    {
        "search":"search_email",
        "search_by":"email"
    }
    ```





