# Task Master

A simple and efficient task management web application built with Flask and SQLite.

## Features

- Create, read, update, and delete tasks
- Clean and responsive user interface
- Tasks are sorted by creation date
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

- **Add a task**: Type your task in the input field and press Enter or click the "Add Task" button
- **Update a task**: Click the "Update" button next to the task you want to modify
- **Delete a task**: Click the "Delete" button next to the task you want to remove

## Project Structure

```
Task-Master/
├── instance/
│   └── database.db        # SQLite database file
├── static/
│   └── css/
│       ├── main.css       # Custom styles
│       └── bootstrap.min.css  # Bootstrap CSS
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Main page template
│   └── update.html       # Update task template
├── app.py               # Main application file
└── requirements.txt     # Python dependencies
```

## Dependencies

- Flask 3.1.0
- Flask-SQLAlchemy 3.1.1
- SQLAlchemy 2.0.25
- Werkzeug 3.0.1
- Jinja2 3.1.3
- itsdangerous 2.1.2

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
