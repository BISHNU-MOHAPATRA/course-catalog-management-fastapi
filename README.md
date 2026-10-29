# Course Catalog Management System — FastAPI

A REST API for managing courses and student enrollments, built with Python, FastAPI, SQLAlchemy, and SQLite/MySQL.

## Features
- Course CRUD endpoints
- Student enrollment CRUD endpoints
- SQLAlchemy ORM models
- Interactive API documentation with Swagger UI
- SQLite default for quick local setup; MySQL configurable through `DATABASE_URL`

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite / MySQL
- Uvicorn

## Run locally

1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment:

   Windows:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the API:

   ```bash
   uvicorn main:app --reload
   ```

6. Open:
   - API welcome page: http://127.0.0.1:8000/
   - Swagger API docs: http://127.0.0.1:8000/docs

## Main endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/courses/` | List courses |
| POST | `/courses/` | Create a course |
| GET | `/courses/{course_id}` | Get one course |
| PUT | `/courses/{course_id}` | Update a course |
| DELETE | `/courses/{course_id}` | Delete a course |
| GET | `/enrollments/` | List enrollments |
| POST | `/enrollments/` | Create an enrollment |
| GET | `/enrollments/{enrollment_id}` | Get one enrollment |
| PUT | `/enrollments/{enrollment_id}` | Update an enrollment |
| DELETE | `/enrollments/{enrollment_id}` | Delete an enrollment |

## Configure MySQL (optional)

Set the `DATABASE_URL` environment variable before starting the API, using your own local credentials. Do not commit passwords or `.env` files to GitHub.

Example format:

```text
mysql+pymysql://YOUR_USER:YOUR_PASSWORD@localhost/fastapi_project
```

The tables are created automatically when the application starts. Ensure the target database exists before connecting.

## Notes
- This repository contains source code only; virtual environments, compiled Python files, and local database files are excluded.
- The React frontend is not included in this backend repository.
- Before production deployment, configure a managed database, CORS origins, and environment variables for the deployment platform.
