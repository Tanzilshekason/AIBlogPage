# Blog Application

A full-featured blog platform built with Python and Django. This application allows users to view, create, edit, and delete blog posts, complete with user authentication and an intuitive user interface.

## 🚀 Features

- **Blog Post Management**: Complete CRUD (Create, Read, Update, Delete) functionality for blog posts.
- **User Authentication**: Secure sign up, log in, and session management.
- **Rich Content**: Each post tracks the title, content, author, and timestamp.
- **Navigation & Pagination**: Easy navigation between posts with pagination controls.
- **Server-Side Rendering**: Fast and SEO-friendly pages rendered on the server using Django templates.
- **Responsive UI**: Built with HTML, CSS, and JavaScript for a great experience on any device.

## 🛠️ Technology Stack

- **Backend**: Python, Django 5.x
- **Database**: SQLite (Development)
- **Frontend**: HTML, CSS, JavaScript
- **User Authentication**: Django Auth System

## ⚙️ Setup and Installation

Follow these steps to get your development environment running:

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd /path/to/Blogapp
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   *(Assuming a `requirements.txt` is present, otherwise install Django manually if creating a fresh environment)*
   ```bash
   pip install django
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (so you can access the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Website: [http://127.0.0.hofst/](http://127.0.0.1:8000/)
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 🧪 Testing

The project includes unit tests for the backend logic and integration tests for routes and templates to ensure software quality. To run the tests, execute:
```bash
python manage.py test
```

## 🔒 Security

Built with Django's robust security features in mind, including:
- Input sanitization
- Cross-Site Request Forgery (CSRF) protection
- Cross-Site Scripting (XSS) prevention

## 📝 Project Boundaries Note

As per the established project boundaries:
- Code is structured to be modular and maintainable.

---
*Built with ❤️ using Django.*
