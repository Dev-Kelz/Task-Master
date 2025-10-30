# Task Master

A modern and efficient task management web application built with a professional, production-ready stack.

This project demonstrates best practices in application structure, containerization, and frontend development, making it a perfect showcase piece for a software development portfolio.

## Features

- **User Authentication**: Secure registration, login, and session management.
- **Task Management**: Full CRUD (Create, Read, Update, Delete) functionality for user-specific tasks.
- **Modern UI**: A clean, responsive, and intuitive user interface built with **Tailwind CSS**.

## Technical Stack

- **Backend**: Flask
- **Database**: SQLite (with support for PostgreSQL)
- **Frontend**: Tailwind CSS
- **Containerization**: Docker & Docker Compose
- **WSGI Server**: Gunicorn

## Project Structure

This application is structured using the **Application Factory** pattern and **Blueprints** to ensure scalability and maintainability.

```
Task-Master/
|-- project/                # Main application package
|   |-- __init__.py         # Application factory
|   |-- auth.py             # Auth blueprint (routes)
|   |-- main.py             # Main blueprint (routes)
|   |-- models.py           # SQLAlchemy models
|   |-- forms.py            # WTForms classes
|   |-- static/
|   `-- templates/
|-- .env                    # Environment variables (SECRET_KEY, etc.)
|-- .gitignore
|-- docker-compose.yml      # Docker Compose configuration
|-- Dockerfile              # Multi-stage Docker build
|-- package.json            # Frontend dependencies
|-- tailwind.config.js      # Tailwind CSS configuration
|-- requirements.txt        # Python dependencies
`-- run.py                  # Application entry point
```

## Getting Started

This application is fully containerized, so the only prerequisite is **Docker**.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Running

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Dev-Kelz/Task-Master.git
    cd Task-Master
    ```

2.  **Create the environment file**:
    Create a file named `.env` in the root directory. This file will hold your secret configuration.

3.  **Add environment variables**:
    Open the `.env` file and add the following line. **Replace the placeholder with a strong, random string.**
    ```
    SECRET_KEY='your_super_secret_and_random_key_here'
    ```

4.  **Build and run the application**:
    Use Docker Compose to build the images and start the services.
    ```bash
    docker-compose up --build
    ```

5.  **Access the application**:
    Open your web browser and navigate to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

## License

This project is open source and available under the [MIT License](LICENSE).
