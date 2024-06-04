
# Django Migrations Practice Project

This is a practice project using Django to work with migrations and a basic set of routes. The project includes a SQLite database and three main routes.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

## Routes

The project includes the following routes:

- **/admin/**: Django admin interface.
- **/flight/**: Main page to list flights.
- **/flight/<id>/**: Detail page for a specific flight.

## Project Description

This project is a practice exercise for working with migrations in Django. It uses SQLite as the database and provides a basic interface for managing and viewing flights. The main routes allow access to the Django admin panel, list all available flights, and view the details of a specific flight by its ID.

## Migrations

Migrations are a crucial part of Django for handling changes in the database schema. This project includes basic examples of how to create and apply migrations using Django commands.

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher

## How to Contribute

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
