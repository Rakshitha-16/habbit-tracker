# Habit Tracker API

A Django-based backend application for tracking habits. This project exposes a RESTful API to manage habits, utilizing JWT (JSON Web Tokens) for secure authentication.

## Technologies Used

- **Python**: Core programming language.
- **Django**: High-level Python web framework.
- **Django REST Framework**: Toolkit for building Web APIs.
- **Simple JWT**: API Authentication using JSON Web Tokens.
- **SQLite**: Default database for development.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system.

### Installation

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd habbit-tracker
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Based on the project settings, install the required packages:
    ```bash
    pip install django djangorestframework djangorestframework-simplejwt
    ```

4.  **Apply Database Migrations**
    Initialize the SQLite database:
    ```bash
    python manage.py migrate
    ```

5.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```
    The server will start at `http://127.0.0.1:8000/`.

## Configuration

The project settings are located in `habit_tracker/settings.py`.

*   **Authentication**: JWT Access tokens expire in 30 minutes; refresh tokens expire in 1 day.
*   **Security**: The project is currently configured for development (`DEBUG=True`).
    *   *Note: Before deploying to production, ensure you set `DEBUG=False` and use environment variables for the `SECRET_KEY`.*