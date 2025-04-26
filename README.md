# Todo List Django Application

A sleek, modern Todo app built with Django, featuring a cyberpunk-inspired UI.

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```
   python manage.py migrate
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```

## Deployment to Render

### Automatic Deployment with render.yaml

1. Push your code to a Git repository (GitHub, GitLab, etc.)
2. Create a new account or log in to [Render](https://render.com/)
3. Click "New" and select "Blueprint" 
4. Connect your Git repository
5. Render will automatically deploy your application using the configuration in `render.yaml`

### Manual Deployment

1. Push your code to a Git repository (GitHub, GitLab, etc.)
2. Create a new account or log in to [Render](https://render.com/)
3. Click "New" and select "Web Service"
4. Connect your Git repository
5. Configure your service:
   - Name: todo-app (or your preferred name)
   - Runtime: Python
   - Build Command: `./build.sh`
   - Start Command: `gunicorn todo_list.wsgi:application`
6. Add Environment Variables:
   - `SECRET_KEY`: Generate a secure random key
   - `DEBUG`: false
   - `DATABASE_URL`: This will be automatically set if you create a Render PostgreSQL database

7. Create a PostgreSQL database:
   - Go to Dashboard > New > PostgreSQL
   - Connect your web service to this database

## Features

- User registration and authentication
- Create, read, update, and delete todo items
- Mark tasks as complete
- Beautiful cyberpunk-inspired UI
- Responsive design for mobile and desktop 