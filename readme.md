
## JSONPlaceholder API Test Automation Project

**This document is in English. For the Turkish version, please click [README_TR.md](README_TR.md).**

This project is an **API Test Automation** system developed to test RESTful requests on the fake API service [JSONPlaceholder](https://jsonplaceholder.typicode.com/). The project uses Python, `pytest`, and `requests` libraries to test GET, POST, PUT, PATCH, and DELETE requests.

## Features

- Data validation with GET requests  
- Sending and verifying data with POST requests  
- Data update tests with PUT and PATCH  
- Delete operation tests with DELETE  
- Test scenarios implemented using `pytest`  
- Test results logged to a file  
- Clean code organization with a structure similar to POM (Page Object Model)

## Project Structure

```bash
├── api_json.py               # Class managing API operations (GET, POST, PUT, PATCH, DELETE)
├── test_api_response.py      # API test scenarios
├── test_post_operations.py   # POST, PUT, PATCH, DELETE tests
├── test_log.log              # File containing test logs
├── conftest.py               # Pytest logging configuration
└── README.md                 # This file
````

## Installation

> Python 3 must be installed before running this project.

```pip install requests pytest```

## Running Tests

Run all tests in the terminal with:

```pytest```

Test outputs are saved in the log file: `test_log.log`

## Sample Tests

* `GET /posts/1` → Verify post content by ID
* `GET /posts/1/comments` → Check comments for a post
* `POST /posts` → Create a new post
* `PUT /posts/1` → Update entire content
* `PATCH /posts/1` → Update only specific fields
* `DELETE /posts/1` → Delete a specific post

## Technologies Used

* Python
* Requests
* Pytest
* JSONPlaceholder (Fake REST API)

## Notes

* This project sends requests to a fake REST API designed for testing purposes, not a real API.
* JSONPlaceholder does not actually modify data on the server (POST, PUT, DELETE operations run as simulations).


**Author**: Erkut Elik
**GitHub**: https://github.com/erkutelk


