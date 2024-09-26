# AcadevaSync - Online Learning Management System

**AcadevaSync** is an online learning management system (LMS) built using Django. The platform is designed to support educators, students, and administrators in managing courses, content, and assessments efficiently. AcadevaSync offers tools for student engagement, assignment submissions, progress tracking, and more.

## Features

- **User Roles**: Support for students, instructors, and administrators with tailored access levels.
- **Course Management**: Create and manage courses, modules, and lesson plans with rich multimedia content.
- **Login & registration form**: login and registration and password reset system for student safety.
- **Announcements**: Instructors can post important updates and notifications to their students.
- **Responsive Design**: Fully optimized for desktop, tablet, and mobile devices.
- **Admin Dashboard**: Comprehensive control over course management, user roles, and platform settings.

## Technologies Used

- **Backend**: Django, Django Rest Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (depending on environment)
- **Other Libraries**: Pillow (for image uploads), Crispy Forms (for form styling), Celery (for task scheduling)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- SQLite
- pip (Python package installer)

```bash
  -pip install -r requirements.txt
```

### Steps to Install

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/acadevasync.git
    ```

2. Navigate to the project directory:
    ```bash
    cd acadevasync
    ```

3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install required dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up the database:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the server:
    ```bash
    python manage.py runserver
    ```

8. Access the website at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Project Structure


## 🛠 Skills
Django, Python, Javascript, HTML, CSS, BootStrap...

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/itsme-kps/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/kp_8618)
