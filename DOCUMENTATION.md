# API Documentation

## Introduction

Welcome to the documentation for the RESTful API for managing person records. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on person resources. Below, you'll find information on how to use the API, including endpoints, request formats, and sample usage.

## Base URL

The base URL for accessing the API is: `https://your-api-domain.com/api`

## Authentication

Authentication is required to access certain endpoints. You should include an API token in the request headers for authentication. Please contact the API administrator to obtain an API token.

## Person Resource

### Create a New Person

- **Endpoint:** `/person`
- **HTTP Method:** POST
- **Request Body:**
    ```json
    {
       "name": "John Doe",
       "age": 30,
       "email": "johndoe@example.com"
    }
    ```
- **Response (Success):** HTTP 201 Created
    ```json
    {
       "id": 1,
       "name": "John Doe",
       "age": 30,
       "email": "johndoe@example.com"
    }
    ```
- **Response (Validation Error):** HTTP 400 Bad Request
    ```json
    {
       "errors": {
           "name": ["This field is required."],
           "age": ["Age must be a positive integer."]
       }
    }
    ```

### Retrieve a Person by Name

- **Endpoint:** `/person/{name}`
- **HTTP Method:** GET
- **Response (Success):** HTTP 200 OK
    ```json
    {
       "id": 1,
       "name": "John Doe",
       "age": 30,
       "email": "johndoe@example.com"
    }
    ```
- **Response (Not Found):** HTTP 404 Not Found
    ```json
    {
       "detail": "Person not found."
    }
    ```

### Update a Person by Name

- **Endpoint:** `/person/{name}`
- **HTTP Method:** PUT
- **Request Body:**
    ```json
    {
       "age": 31
    }
    ```
- **Response (Success):** HTTP 200 OK
    ```json
    {
       "id": 1,
       "name": "John Doe",
       "age": 31,
       "email": "johndoe@example.com"
    }
    ```
- **Response (Validation Error):** HTTP 400 Bad Request
    ```json
    {
       "errors": {
           "age": ["Age must be a positive integer."]
       }
    }
    ```

### Delete a Person by Name

- **Endpoint:** `/person/{name}`
- **HTTP Method:** DELETE
- **Response (Success):** HTTP 204 No Content
- **Response (Not Found):** HTTP 404 Not Found
    ```json
    {
       "detail": "Person not found."
    }
    ```

## Error Handling

The API provides detailed error messages in the response body when validation or other errors occur. Always check the response status code and the response body for error details.

## Rate Limiting

To ensure fair usage of the API, rate limiting is enforced. Please refer to the API rate limits specified in the response headers.

## Conclusion

This API documentation provides an overview of the available endpoints and how to interact with the API. For additional information or support, please contact the API administrator.

Remember to replace placeholders such as `https://your-api-domain.com/api` with the actual base URL of your API and customize the documentation according to your API's specific endpoints and response formats.