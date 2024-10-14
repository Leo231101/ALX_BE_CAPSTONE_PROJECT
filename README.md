I've created a detailed README file for your Django E-commerce API. It covers user accounts, products, wishlists, reviews, and discounts. This guide is designed to help you understand the API and how to interact with it effectively.

---

# E-commerce API

The API has been constructed using Django and Django REST Framework to drive an e-commerce platform. It delivers essential functionalities, encompassing user authentication, product management, reviews, wishlists, and discounts.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup and Installation](#setup-and-installation)
3. [Authentication](#authentication)
4. [Endpoints](#endpoints)
   - [Users (Accounts)](#users-accounts)
   - [Products](#products)
   - [Wishlists](#wishlists)
   - [Reviews](#reviews)
   - [Discounts](#discounts)
5. [Testing the API](#testing-the-api)
6. [Contribution Guidelines](#contribution-guidelines)
7. [License](#license)

---

## Project Overview

This API enables users to:

- Register, log in, and manage their accounts.
- Create, update, and delete products.
- Order products and manage stock.

---

## Setup and Installation

### Prerequisites

- Python 3.8+
- Django 4.2+
- Django REST Framework
- PostgreSQL (or SQLite for development)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/e_commerce_api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd e_commerce_api
   ```

3. Create a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

4. Install the required packages:

   ```bash
   pip install django
   ```

5. Configure your database in `settings.py` (SQLite is default, but PostgreSQL can be used in production).

6. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the API at `http://127.0.0.1:8000/`

---

## Authentication

To access the API's features, users are required to authenticate using a token. This token-based authentication method is necessary for interactions with most endpoints. To authenticate, users can either log in with their existing credentials or create a new account
---

## Endpoints

### 1. **Users (Accounts)**

#### Register a New User

- **URL**: `/api/accounts/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "newuser",
    "password": "newpassword",
    "email": "newuser@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "token": "your_token"
  }
  ```

#### User Login

- **URL**: `/api/accounts/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "newuser",
    "password": "newpassword",
    "email": "newuser@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "token": "your_token"
  }
  ```

---

Include the token in the Authorization header for authenticated requests:

```bash
Authorization: Token your_token
```

---

### 2. **Products**

#### List All Products

- **URL**: `/api/products/`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Product 1",
      "description": "A detailed description",
      "price": 99.99,
      "category": {
        "name": "Electronics",
        "description": "Category for electronic items"
      },
      "stock_quantity": 50,
      "images": [
        {
          "image_url": "http://example.com/image1.jpg"
        },
        {
          "image_url": "http://example.com/image2.jpg"
        }
      ],
      "created_date": "2024-10-01"
    }
  ]
  ```

#### Create a New Product

- **URL**: `/api/products/`
- **Method**: `POST`
- **Authentication Required**: Yes
- **Request Body**:
  ```json
  {
    "name": "Product 1",
    "description": "A detailed description",
    "price": 99.99,
    "category": {
      "name": "Electronics",
      "description": "Category for electronic items"
    },
    "stock_quantity": 50,
    "images": [
      {
        "image_url": "http://example.com/image1.jpg"
      },
      {
        "image_url": "http://example.com/image2.jpg"
      }
    ]
  }
  ```

#### Retrieve a Product by ID

- **URL**: `/api/products/{id}/`
- **Method**: `GET`

#### Update a Product by ID

- **URL**: `/api/products/{id}/`
- **Method**: `PUT` or `PATCH`

#### Delete a Product by ID

- **URL**: `/api/products/{id}/`
- **Method**: `DELETE`

---

#### Product Search

- **URL**: `/api/products/search/`
- **Method**: `GET`
- **Query Parameters**:
  - `name`: (optional) Partial name to search for products.
  - `category`: (optional) Filter products by category.
  - `price_min`: (optional) Minimum price for filtering.
  - `price_max`: (optional) Maximum price for filtering.
  - `page`: (optional) Page number for pagination (default is 1).
  - `page_size`: (optional) Number of products per page (default is 10).
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Product 1",
      "description": "A detailed description",
      "price": 99.99,
      "category": {
        "name": "Electronics",
        "description": "Category for electronic items"
      },
      "stock_quantity": 50,
      "images": [
        {
          "image_url": "http://example.com/image1.jpg"
        }
      ],
      "created_date": "2024-10-01"
    }
  ]
  ```

---

### 3. **Orders**

#### Create a New Order

The stock quantity is reduced if the order is validated.

- **URL**: `/api/order/`
- **Method**: `POST`
- **Authentication Required**: Yes
- **Request Body**:

  ```json
  {
    "product": 1, // ID of the product to order
    "quantity": 2 // Quantity of the product to order
  }
  ```

- **Response** (Success - 201 Created):

  ```json
  {
    "order_id": 1,
    "product": 1,
    "quantity": 2
  }
  ```
