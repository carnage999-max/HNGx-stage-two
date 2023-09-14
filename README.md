# Person API Documentation

## Table of Contents

- [Introduction](#introduction)
  - [Base URL](#base-url)
  - [Person Model](#person-model)
    - [UML diagram](#uml-diagram-for-the-person-model)
- [Endpoint formats](#endpoints-formats)
  - [Create Person](#create-a-new-person)
  - [Get a person](#retrieve-a-person-by-id)
  - [Update a person by ID](#update-a-person-by-id)
  - [Delete a person](#delete-a-person-by-id)
- [Local Development Setup](#local-development-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Development Server](#running-the-development-server)
- [Conclusion](#conclusion)

## Introduction

Welcome to the documentation for the RESTful API for managing `person` records. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on person resources. Below, you'll find information on how to use the API, including endpoints, request formats, and sample usage.

## Base URL

Read the documentation for the api at [https://hngtask11011.pythonanywhere.com](https://hngtask11011.pythonanywhere.com)

The URL for accessing the API is: [https://hngtask11011.pythonanywhere.com/api](https://hngtask11011.pythonanywhere.com/api)

# Person Model

The `Person` model represents individuals in our database. It stores information about each person, including their name and the date they were created in the database.

## Model Fields

- **`id`** (Auto-generated primary key, integer): This field is an auto-generated primary key, serving as a unique identifier for each person in the database.

- **`name`** (String): This field stores the name of the person as a string. It represents the person's full name.

- **`date_created`** (Auto-generated timestamp): This field is an auto-generated timestamp that records the date and time when the person record was created in the database. It provides information about when the person was added to our system.

### Example Person

```json
  {
       "id": 1,
       "name": "John Doe",
       "date_created": "2023-09-13T16:40:22.396820Z"
  }
```

## UML Diagram for the `Person` Model

![Person Model UML Diagram](https://i.ibb.co/wgbhzyN/person-uml-diagram-drawio.png)

### Class: `Person`

The UML diagram represents the `Person` model, which is used to store information about individuals in the system.
There are no other tables in the database. Hence, no relationships between tables.

- `+ id: int (PK)`\
   The `id` field is an auto-generated primary key, represented as an integer. It uniquely identifies each person record in the database.

- `+ name: str`\
   The `name` field is a string that stores the name of the person. It can contain the person's full name or any other name-related information.

- `+ date_created: datetime`\
   The `date_created` field is an auto-generated timestamp that indicates when the `Person` record was created in the database. It stores date and time information.

---

## Endpoints formats

### Create a New Person

- **Endpoint:** `/api`
- **HTTP Method:** POST
- **Request Body:**

    ```json
    {
       "name": "John Doe"
    }
    ```

- **Response (Success):** HTTP 201 Created

    ```json
    {
       "id": 1,
       "name": "John Doe",
       "date_created": "2023-09-13T16:40:22.396820Z"
    }
    ```

- **Response (Validation Error):** HTTP 400 Bad Request

    ```json
    {
       "errors": {
           "name": ["This field is required."]
       }
    }
    ```

### Retrieve a Person by ID

- **Endpoint:** `/api/id`
    ```

- **Response (Success):** HTTP 200 OK

    ```json
    {
       "id": 1,
       "name": "John Doe",
       "date_created": "2023-09-13T16:40:22.396820Z"
    }
    ```

- **Response (Not Found):** HTTP 404 Not Found

    ```json
    {
       "error": "A user with ID, 1, does not exist"
    }
    ```

### Update a Person by id

- **Endpoint:** `/api/id`
- **HTTP Method:** PUT
- **Request Body:**

    ```json
    {
       "name": "Jon Snow"
    }
    ```

- **Response (Success):** HTTP 200 OK

    ```json
    {
       "id": 1,
       "name": "Jon Snow",
       "date_created": "2023-09-13T16:40:22.396820Z"
    }
    ```

- **Response (Validation Error):** HTTP 400 Bad Request

    ```json
    {
       "errors": {
           "name": ["name should be a string value"]
       }
    }
    ```

### Delete a Person by ID

- **Endpoint:** `/api/id`
- **HTTP Method:** DELETE
- **Response (Success):** HTTP 204

    ```json
    {
       "response": "Person Deleted Successfully"
    }
    ```

- **Response (Not Found):** HTTP 404 Not Found

## Local Development Setup

## Prerequisites

Before you begin, ensure that you have the following software installed on your local development machine:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Django: [Install Django](https://docs.djangoproject.com/en/stable/intro/install/)
- Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/carnage999-max/HNGx-stage-two.git
   ```

2. Navigate to the project directory:

  ```bash
    cd your-api-name
  ```

3. Create a virtual environment:

  ```bash
    python -m venv venv
  ```

4. Activate the virtual environment:

- On Windows:

  ```bash
    venv\Scripts\activate
  ```

- On MacOS and Linux:

  ```bash
  source venv/bin/activate
  ```

5. Install the project dependencies:

  ```bash  
  pip install -r requirements.txt
  ```

### Running the Development Server

1. Apply migrations to create the database schema:

    bash

    ```bash
    python manage.py migrate
    ```

2. Create a superuser account for admin access (follow the prompts):

    bash

    ```bash
    python manage.py createsuperuser
    ```

3. Start the development server:

    bash

    ```bash
    python manage.py runserver
    ```

4. Access the API in your web browser at `http://localhost:8000/` and the Django admin interface at `http://localhost:8000/admin/`. Log in with your superuser credentials.

---

## Conclusion

This API documentation provides an overview of the available endpoints and how to interact with the API. For additional information or support, please contact the [API administrator](mailto:ezekielokebule11011@outlook.com)

---

# [Back to top](#table-of-contents)
