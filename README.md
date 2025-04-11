# Book Haven - Django Bookstore

A modern Django-based online bookstore with user authentication, shopping cart functionality, and book management.

## Features

- User Authentication (Login/Logout)
- Book Catalog with Search
- Shopping Cart
- Book Categories
- Responsive Design
- Admin Interface for Book Management

## Technologies Used

- Django 5.2
- Python 3.13
- Bootstrap 5
- SQLite Database
- Font Awesome Icons

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/book-haven.git
cd book-haven
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application at http://127.0.0.1:8000/

## Project Structure

```
bookstore/
├── accounts/          # User authentication app
├── store/            # Main bookstore app
│   ├── migrations/   # Database migrations
│   ├── templates/    # HTML templates
│   ├── models.py     # Database models
│   ├── views.py      # View functions
│   └── urls.py       # URL routing
├── media/            # User uploaded files
├── static/           # Static files
└── bookstore/        # Project settings
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 