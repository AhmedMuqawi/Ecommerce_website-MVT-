# Ecommerce_website-MVT-

# E-commerce Website

This is a Django-based e-commerce website built using the MVT (Model-View-Template) architecture. It includes authentication, cart functionality, and role-based product management for admins and users.

## Features

-   User authentication (Login, Logout, Register)
-   Shopping cart (Users can add and view items)
-   Only admins can delete products
-   Logged-in users can add/edit products and categories

## Installation

### 1. Set Up a Virtual Environment

It is recommended to create a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

-   **Windows**: `venv\Scripts\activate`
-   **Mac/Linux**: `source venv/bin/activate`

### 2. Install Dependencies

After activating the virtual environment, install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 4. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Now, you can access the e-commerce website at `http://127.0.0.1:8000/`.

## Admin Access

To access the admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up an admin account, then log in at `http://127.0.0.1:8000/admin/`.

## License

This project is for educational purposes and can be modified as needed.
