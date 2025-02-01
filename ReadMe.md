# TodoApp

TodoApp is a Django-based web application designed to help users manage their tasks and events efficiently. The application provides a user-friendly interface for adding, updating, and deleting tasks, along with user authentication and search functionality.

## Features

- **User Registration and Authentication**: Secure user registration and login functionality.
- **Task Management**: Add, update, and delete tasks/events.
- **Search Functionality**: Search tasks by title.
- **Task Completion**: Mark tasks as done.
- **Responsive Design**: Mobile-friendly interface.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 5.1.4
- Virtualenv

### Steps

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/TodoApp.git
    cd TodoApp
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv myenv
    source myenv/Scripts/activate  # On Windows
    source myenv/bin/activate      # On Unix or MacOS
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Register**: Create a new user account.
- **Login**: Access your account using your credentials.
- **Add Event**: Use the "Add Event" button to create a new task/event.
- **Manage Events**: View, update, or delete tasks/events from the main page.
- **Search**: Use the search bar to filter tasks by title.
- **Mark as Done**: Check the checkbox next to each task to mark it as done.

## Project Structure

- [TodoApp](http://_vscodecontentref_/1): Main project directory
  - [events/](http://_vscodecontentref_/2): Contains the event-related models, views, and templates
    - [admin.py](http://_vscodecontentref_/3): Admin configuration for the Event model
    - [apps.py](http://_vscodecontentref_/4): Application configuration
    - [forms.py](http://_vscodecontentref_/5): Forms for event creation and update
    - [migrations/](http://_vscodecontentref_/6): Database migrations
    - [models.py](http://_vscodecontentref_/7): Event model definition
    - [tests.py](http://_vscodecontentref_/8): Unit tests for the events app
    - [urls.py](http://_vscodecontentref_/9): URL routing for the events app
    - [views.py](http://_vscodecontentref_/10): Views for handling event-related requests
  - `static/`: Contains static files (CSS, JavaScript)
  - `templates/`: Contains HTML templates
  - [TodoApp](http://_vscodecontentref_/11): Contains project settings, URLs, and views
    - [settings.py](http://_vscodecontentref_/12): Project settings
    - [urls.py](http://_vscodecontentref_/13): URL routing for the project
    - [views.py](http://_vscodecontentref_/14): Views for handling user authentication and main page
    - [wsgi.py](http://_vscodecontentref_/15): WSGI configuration for deployment
    - [asgi.py](http://_vscodecontentref_/16): ASGI configuration for deployment
  - [manage.py](http://_vscodecontentref_/17): Django's command-line utility for administrative tasks
  - [db.sqlite3](http://_vscodecontentref_/18): SQLite database file

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them ([git commit -m 'Add new feature'](http://_vscodecontentref_/19)).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or support, please contact [yourname@example.com](mailto:yourname@example.com).