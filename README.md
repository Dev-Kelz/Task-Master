# Task Master

A simple and efficient task management web application built with Flask and SQLite.

## Features

- **User Authentication**
  - Secure user registration and login
  - Password hashing for security
  - Protected routes for authenticated users only
- **Task Management**
  - Create, read, update, and delete tasks
  - Tasks are sorted by creation date
  - User-specific task management
- **Technical**
  - Clean and responsive user interface
  - Persistent storage using SQLite database
  - Built with Flask and SQLAlchemy

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dev-Kelz/Task-Master.git
   cd Task-Master
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Initialize the database**
   ```bash
   python -c "from app import app, db; app.app_context().push(); db.create_all()"
   ```

2. **Start the development server**
   ```bash
   python app.py
   ```

3. **Open your web browser and navigate to**
   ```
   http://127.0.0.1:5000/
   ```

## Usage

### Authentication
1. **Register** a new account by clicking the "Register" link in the navigation bar
2. **Login** with your credentials
3. **Logout** when you're done to secure your account

### Task Management
- **Add a task**: Type your task in the input field and press Enter or click the "Add Task" button
- **Update a task**: Click the "Update" button next to the task you want to modify
- **Delete a task**: Click the "Delete" button next to the task you want to remove

> **Note**: You must be logged in to manage tasks. Each user can only view and modify their own tasks.

## Project Structure

```
Task-Master/
├── instance/
│   └── database.db            # SQLite database file
├── static/
│   └── css/
│       ├── main.css           # Custom styles
│       ├── tasks.css          # Task-specific styles
│       └── bootstrap.min.css  # Bootstrap CSS
├── templates/
│   ├── base.html             # Base template with navigation
│   ├── index.html            # Main tasks page template
│   ├── login.html            # User login page
│   ├── register.html         # User registration page
│   ├── update.html           # Task update template
│   ├── welcome.html          # Welcome/landing page
│   ├── 404.html              # 404 error page
│   └── 500.html              # 500 error page
├── app.py                   # Main application file
└── requirements.txt         # Python dependencies
```

## Dependencies

- Flask==3.1.0
- Flask-Login==0.6.3
- Flask-SQLAlchemy==3.1.1
- Flask-WTF==1.2.1
- SQLAlchemy==2.0.36
- Werkzeug==3.1.3
- Jinja2==3.1.4
- itsdangerous==2.2.0
- email-validator==2.1.0.post1
- gunicorn==23.0.0  # For production deployment
- blinker==1.9.0  # For flash messages
- click==8.1.7  # Command Line Interface Creation Kit
- greenlet==3.1.1  # SQLAlchemy concurrency support

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
