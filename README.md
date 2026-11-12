StudyTrack
Overview

StudyTrack is a personal study planner web application built using Python 
and Django. It helps students organize their academic workload by creating 
study tasks, assigning subjects, setting deadlines, and tracking task 
completion.

The goal of StudyTrack is to make managing schoolwork easier by providing 
a simple and organized place to keep track of assignments and study 
responsibilities.

Distinctiveness and Complexity

StudyTrack is distinct from the other CS50 Web Programming projects 
because it focuses on personal academic productivity rather than social 
networking, online shopping, or discussion forums.

Unlike a basic to-do list, StudyTrack organizes tasks around academic 
subjects and deadlines. Users can create study tasks, view them in 
deadline order, mark them as completed, and delete tasks when they are no 
longer needed.

The application uses Django models to store tasks in a database. Each task 
includes a title, subject, deadline, completion status, and creation date. 
Django views handle the application logic, while Django templates display 
the information to the user.

The application also includes separate functions for adding, completing, 
and deleting tasks. These features require communication between the front 
end and back end through HTTP requests and Django URL routing.

The interface is designed to be simple and responsive, making it 
accessible on different screen sizes.

Files and Directories
manage.py: Main Django command-line utility.
requirements.txt: Lists the Python packages required to run the 
application.
config/: Contains the main Django project configuration.
config/settings.py: Contains application settings and installed apps.
config/urls.py: Defines the main URL configuration.
config/asgi.py: ASGI configuration.
config/wsgi.py: WSGI configuration.
planner/models.py: Defines the Task database model.
planner/views.py: Handles creating, displaying, completing, and deleting 
tasks.
planner/urls.py: Defines URLs for the planner application.
planner/admin.py: Registers models for Django administration.
planner/apps.py: Contains application configuration.
planner/tests.py: Contains the application's test file.
planner/templates/planner/index.html: Contains the HTML and CSS for the 
StudyTrack interface.
planner/migrations/: Contains database migration files.
How to Run the Application
Install Python 3.
Clone or download the project.
Navigate to the project directory.
Create and activate a virtual environment.
Install dependencies:

python -m pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Start the Django development server:

python manage.py runserver

Open http://127.0.0.1:8000/ in a web browser.
Additional Information

StudyTrack uses Django and SQLite. The application allows users to add 
study tasks with subjects and deadlines, mark tasks as completed or 
pending, and delete tasks.

The Django administration interface is also available at /admin/ for 
managing database records.

This project was created as the final project for CS50's Web Programming 
with Python and JavaScript.
