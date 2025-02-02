Multilingual FAQ System with WYSIWYG Support 🌍📑
Welcome to the Multilingual FAQ System! This project provides a powerful FAQ platform that supports multiple languages and integrates with a WYSIWYG editor for better content management. 🚀

Features ✨
Multilingual Support: FAQs can be translated into multiple languages (English, Hindi, Bengali, Swahili, etc.) using the Google Translate API.
WYSIWYG Editor: A Rich Text Editor (django-ckeditor) for managing and formatting the answers.
API Endpoints: A fully functional API to fetch FAQs based on language preferences.
Caching with Redis: FAQs are cached in Redis to provide faster responses.
Admin Panel: A user-friendly Django admin interface to manage FAQs.
Pagination: Pagination support for FAQ listings.
Technologies Used 🛠️
Django 3.2+: Backend Framework
django-ckeditor: For WYSIWYG editor integration
Google Translate API: For multilingual support
Redis: Caching system for improved performance
Django REST Framework: For creating API endpoints
SQLite / PostgreSQL / MySQL: Database support
Python 3.8+
Installation ⚡
To get started with this project, follow the instructions below.

Prerequisites 📦
Python 3.8+
Django 3.2+
Redis (for caching)
Steps to Set Up 🏗️
Clone the Repository:

git clone https://github.com/punnayansaha07/multilingual-faq.git
cd multilingual-faq
Install Dependencies:

Ensure you have pip installed. Run the following command to install all required packages:

pip install -r requirements.txt
Set Up Database:

If you're using PostgreSQL, MySQL, or SQLite, you may need to adjust your database settings in settings.py. The default configuration is set for SQLite.

Run Migrations:

After setting up the database, run the migrations to create the necessary tables:

python manage.py migrate
Start Redis (Optional, if you're using Redis):

If you are using Redis for caching, make sure Redis is running on your machine:

redis-server
Run the Development Server:

Start the Django development server:

python manage.py runserver
Visit http://127.0.0.1:8000/ to see the application in action.

Docker Setup (Optional) 🐳
If you want to deploy this project with Docker, follow these steps:

Build and Run Docker Containers:

You can use the docker-compose.yml file to build and run the Docker containers for the project:

docker-compose up --build
Access the Application:

Once the Docker containers are running, visit the application in your browser at:

http://localhost:8000
Usage 📖
Admin Panel 🎛️
You can manage the FAQs directly through the Django Admin panel. To access it, run the development server and navigate to:

http://127.0.0.1:8000/admin
Login using the admin credentials you created. You’ll be able to:

Add, edit, and delete FAQ entries.
Manage translations for each FAQ.
Adding a New FAQ:
Go to the Django Admin Panel.
Navigate to the FAQ model.
Add a new FAQ entry by filling in the Question and Answer fields.
Optionally, provide translations for the FAQ in various languages.
Using the API 📡
This project provides an API endpoint to fetch FAQs. You can access it by making a GET request to:

http://127.0.0.1:8000/faqs/?lang=en
Replace lang=en with your preferred language code (e.g., hi, bn, sw).

Example request for Hindi:

http://127.0.0.1:8000/faqs/?lang=hi
API Response:
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "question": "How are you?",
      "answer": "I am good, thank you!",
      "id": 1,
      "created_at": "2025-02-01T06:00:00Z",
      "updated_at": "2025-02-01T06:00:00Z"
    }
  ]
}
Docker Deployment 🚢
Build Docker Image:
To build the Docker image for the application, run:

docker build -t faq-web .
Run Docker Compose:
To start the application with Docker Compose (including all services such as PostgreSQL, Redis, etc.), use:

docker-compose up --build
This will build and run the containers, and you can access your application at http://localhost:8000.
