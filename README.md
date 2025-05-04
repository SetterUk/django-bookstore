# Bookstore Management System

A Django-based web application for managing a bookstore, featuring user authentication, book management, and shopping cart functionality.

## Features

- User Authentication (Registration, Login, Logout)
- Book Management (CRUD operations for staff)
- Shopping Cart with Session-based Storage
- Responsive Design with Bootstrap
- Dockerized Environment
- CI/CD Pipeline with Jenkins

## Tech Stack

- Python 3.8+
- Django 5.2
- PostgreSQL
- Docker & Docker Compose
- Jenkins
- Bootstrap 5

## Prerequisites

- Docker
- Docker Compose
- Python 3.8+
- Git

## Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bookstore.git
cd bookstore
```

2. Create a `.env` file in the project root with the following variables:
```
DEBUG=1
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://bookstore:bookstore123@db:5432/bookstore
```

3. Build and start the containers:
```bash
docker-compose up --build
```

4. Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

5. Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

The application will be available at `http://localhost:8000`

## Project Structure

```
bookstore/
├── accounts/           # User authentication app
├── store/             # Main bookstore app
│   ├── models.py      # Database models
│   ├── views.py       # Class-based views
│   ├── urls.py        # URL routing
│   └── templates/     # HTML templates
├── bookstore/         # Project settings
├── docker-compose.yml # Docker configuration
├── Dockerfile         # Web service configuration
├── Jenkinsfile        # CI/CD pipeline
└── requirements.txt   # Python dependencies
```

## CI/CD Pipeline

The project includes a Jenkins pipeline that:
1. Checks out the code
2. Builds Docker images
3. Runs tests
4. Deploys the application

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 