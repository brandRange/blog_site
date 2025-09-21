📝 Django Blog Project

A simple blog application built with Django that demonstrates the core features of Django’s ORM, views, templates, forms, and authentication system.

🚀 Features

View a list of all blog posts (Homepage).

View details of individual blog posts.

Create new posts using a form.

URLs powered by Django’s urlpatterns and get_absolute_url().

Secure form submissions with CSRF protection.

Admin panel integration for managing posts.

📂 Project Structure
blog_app/
│
├── migrations/       # Database migrations
├── static/           # Static files (CSS, images)
│   └── css/
│       └── base.css
├── templates/        # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── post_detail.html
│   ├── post_delete.html
│   └── post_edit.html
├── models.py         # Post model
├── views.py          # Class-based & function-based views
├── urls.py           # App URL routes
└── tests.py          # Unit tests

⚙️ Setup Instructions

Clone this repo

git clone <https://github.com/brandRange/blog_site.git>
cd blog_app


Create and activate a virtual environment

python -m venv .venv
source .venv/scripts/activate  # Mac/Linux
.venv\Scripts\activate     # Windows, 


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the development server

python manage.py runserver


Visit: http://127.0.0.1:8000/

🛠️ Tech Stack

Backend: Django (Python)

Database: SQLite (default, can be swapped)

Frontend: Django Templates, HTML, CSS

✅ Running Tests
python manage.py test