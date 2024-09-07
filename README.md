![Build Status](https://img.shields.io/github/actions/workflow/status/Alpha-Finance-Tracker/Finance-Tracker-Service/main.yml)
![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![Platform](https://img.shields.io/badge/platform-windows-blue)

# Finance Tracker API

The Finance Tracker API is built to manage financial expenditures and receipt processing. It includes endpoints for registering receipts, adding expenditures, and viewing expenditure history. The application was not built to be used on its own.

## Features
- Upload and process Kaufland receipts.
- Register expenditures for authenticated users.
- Display user expenditure details.
- Secure endpoints using JWT authentication.

## Installation

1. Clone the repository:

   ```bash
   https://github.com/Alpha-Finance-Tracker/Finance-Tracker-Service.git

2. **Install the dependencies:**
   ```bash
     pip install -r requirements.txt

3. **Run the application:**
    ```bash
      uvicorn main:app --reload

Build with docker:
  ```bash
    docker build -t auth_app .
