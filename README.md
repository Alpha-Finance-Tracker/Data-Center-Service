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
4. Build with docker:**
   ```bash
   docker build -t auth_app .

## Endpoints

### 1. Register Kaufland Receipt
**POST** /Finance_tracker/kaufland_receipt

- **Description**:Uploads a Kaufland receipt, processes it using Tesseract and OpenAI. And register it in the database.
- **Request Body**:
  - date: Date when the receipt was issued.
  - image: The receipt image in the form of an uploaded file.
- **Authorization**: JWT token required in the Authorization header.
- **Response**: Confirmation of receipt registration.

### 2. Add Expenditure
**POST** /Finance_tracker/update

- **Description**: Registers an expenditure for the authenticated user.
- **Request Body**:
  - name (str): Name of the expenditure.
  - price (float): Amount spent.
  - category (str): Category of expenditure.
  - expenditure_type (str): Type of expenditure 
  - date (str): Date of the expenditure.
- **Authorization**: JWT token required in the Authorization header.
- **Response**: Confirmation of expenditure registration.

### 3. View Expenditures
**POST** /Finance_tracker/view_expenditures

- **Description**: Retrieves the list of expenditures for the authenticated user.
- **Request Body**:
  - interval (str): The time interval for viewing expenditures (e.g., "monthly", "yearly").
  - column_type (Optional[str]): Type of data column to filter (default: "Optional").
  - category (Optional[str]): Expenditure category to filter by (default: "Optional").
- **Authorization**: JWT token required in the Authorization header.
- **Response**: List of expenditures for the user.

## Authentication

All endpoints are secured using JWT authentication. Make sure to pass the token in the Authorization header as Bearer <token>.
