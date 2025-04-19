# environment_blog
# Environment Blog

A comprehensive Django-based blog application focused on environmental awareness, sustainability, and conservation. This platform allows users to create, read, update, and delete blog posts about environmental topics, categorize content, and access interactive sustainability resources.

![Environment Blog Screenshot](static/images/windmills_hero.jpeg)

## Features

- **User Authentication**: Register, login, and manage user accounts
- **CRUD Operations**: Create, read, update, and delete blog posts
- **Environmental Categories**: Organize content by environmental topics like Climate Change, Renewable Energy, Conservation, etc.
- **Responsive Design**: Bootstrap-based frontend that works on all devices
- **Sustainability Tips**: Dedicated section with practical sustainability advice
- **Environmental Impact Calculator**: Interactive tools to estimate carbon footprint and water usage
- **Rich Text Editing**: Format blog content with images and styling
- **Comment System**: Engage with readers through comments on blog posts
- **Environmental Theme**: Visually appealing design with environmental elements

## Technology Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Heroku
- **Version Control**: Git, GitHub
- **Additional Libraries**:
  - django-crispy-forms
  - Pillow (for image processing)
  - whitenoise (static files)
  - gunicorn (WSGI server)
  - dj-database-url (database configuration)

## Installation

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- virtualenv or venv

### Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/environment_blog.git
   cd environment_blog
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables (create a .env file in the project root):
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key-for-development
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Load initial categories data:
   ```
   python manage.py loaddata blog/fixtures/categories.json
   ```

7. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```
   python manage.py runserver
   ```

9. Access the application at http://127.0.0.1:8000/

## Deployment to Heroku

1. Create a Heroku account and install the Heroku CLI

2. Login to Heroku:
   ```
   heroku login
   ```

3. Create a new Heroku app:
   ```
   heroku create your-app-name
   ```

4. Add PostgreSQL addon:
   ```
   heroku addons:create heroku-postgresql:hobby-dev
   ```

5. Configure environment variables in Heroku:
   ```
   heroku config:set SECRET_KEY=your-production-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

6. Add Heroku as a remote to your Git repository:
   ```
   heroku git:remote -a your-app-name
   ```

7. Push to Heroku:
   ```
   git push heroku main
   ```

8. Run migrations on Heroku:
   ```
   heroku run python manage.py migrate
   ```

9. Load initial data:
   ```
   heroku run python manage.py loaddata blog/fixtures/categories.json
   ```

10. Create a superuser on Heroku:
    ```
    heroku run python manage.py createsuperuser
    ```
## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Bootstrap for the responsive design framework
- Font Awesome for environmental icons
- Pixabay for royalty-free environmental images
- Django community for the excellent web framework
