# FastAPI CRUD Application

## Overview

This FastAPI project provides a simple CRUD (Create, Read, Update, Delete) API for managing items. Each item has attributes including `id`, `name`, `description`, and `price`. The application uses PostgreSQL for the database and SQLAlchemy for ORM.

## Requirements

- Python 3.7+
- PostgreSQL
- Virtual environment (recommended)

## Installation

1. **Clone the Repository:**

    ```sh
    git clone git@github.com:AnjithaTV99/FastAPI_CRUD.git
    cd FastAPI_CRUD
    ```

2. **Create and Activate Virtual Environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  
    # On Windows, use 
    venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**

    Create a `.env` file in the root directory of your project and add the following content:

    ```plaintext
    DB_USERNAME=your_db_username
    DB_PASSWORD=your_db_password
    DB_HOST_NAME=localhost
    DB_PORT=5432
    DB_NAME=your_db_name
    ```

5. **Initialize the Database:**

    Make sure your PostgreSQL server is running and create the database specified in `.env`. The database tables will be created automatically when you run the application.

## Running the Application

To start the FastAPI application, use the following command:

```sh
uvicorn main:app --reload
```

## API Endpoints

### Create an Item

- **Endpoint:** `POST /items/create/`
- **Description:** Create a new item.
- **Request Body:**

    ```json
    {
        "name": "Item Name",
        "description": "Item Description",
        "price": 10.99
    }
    ```
- **Response:**
    ```json
    {
        "status": "success",
        "message": "Item created successfully",
        "data": {
            "id": 1,
            "name": "Item Name",
            "description": "Item Description",
            "price": 10.99
        }
    }
    ```

### Get an Item by ID

- **Endpoint:** `GET /items/get_item_by_id/{id}`
- **Description:** Retrieve an item by its ID.
- **Response:**
    ```json
    {
        "status": "success",
        "message": "Item retrieved successfully",
        "data": {
            "id": 1,
            "name": "Item Name",
            "description": "Item Description",
            "price": 10.99
        }
    }
    ```

### Update an Item by ID

- **Endpoint:** `PUT /items/update_item_by_id/{id}`
- **Description:** Update an existing item by its ID.
- **Request Body:**
    ```json
    {
        "name": "Updated Name",
        "description": "Updated Description",
        "price": 12.99
    }
    ```
- **Response:**
    ```json
    {
        "status": "success",
        "message": "Item updated successfully",
        "data": {
            "id": 1,
            "name": "Updated Name",
            "description": "Updated Description",
            "price": 12.99
        }
    }
    ```

### Delete an Item by ID

- **Endpoint:** `DELETE /items/delete_itm_by_id/{id}`
- **Description:** Delete an item by its ID.
- **Response:**
    ```json
    {
        "status": "success",
        "message": "Item deleted successfully",
        "data": {
            "id": 1,
            "name": "Item Name",
            "description": "Item Description",
            "price": 10.99
        }
    }
    ```

### List All Items

- **Endpoint:** `GET /items//get_items/`
- **Description:** Retrieve a list of all items.
- **Response:**
    ```json
    {
        "status": "success",
        "message": "Items retrieved successfully",
        "data": [
            {
                "id": 1,
                "name": "Item Name",
                "description": "Item Description",
                "price": 10.99
            },
            
        ]
    }
    ```
