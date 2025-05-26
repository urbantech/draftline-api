# DraftLine API

A high-performance API for the DraftLine NIL Management Platform, built with FastAPI and PostgreSQL.

## Features

- User authentication with JWT tokens
- User registration and management
- Secure password hashing
- CORS support
- Environment-based configuration
- SQLAlchemy ORM integration
- Pydantic data validation

## Prerequisites

- Python 3.8+
- PostgreSQL 13+
- pip (Python package manager)

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/draftline-api.git
   cd draftline-api
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file with your database credentials and other settings.

5. **Run database migrations**
   ```bash
   # Install Alembic if not already installed
   pip install alembic
   
   # Run migrations
   alembic upgrade head
   ```

6. **Start the development server**
   ```bash
   ./start.sh
   ```
   The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access the following:

- **Interactive API docs (Swagger UI)**: http://localhost:8000/api/v1/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/api/v1/redoc

## Project Structure

```
draftline-api/
├── app/
│   ├── api/                      # API routes
│   │   ├── api_v1/               # API v1 routes
│   │   ├── deps.py               # Dependencies
│   │   └── endpoints/            # API endpoints
│   ├── core/                     # Core functionality
│   │   ├── config.py             # Configuration settings
│   │   └── security.py           # Security utilities
│   ├── db/                       # Database related code
│   │   ├── crud/                 # CRUD operations
│   │   ├── models/               # SQLAlchemy models
│   │   └── session.py            # Database session
│   ├── schemas/                  # Pydantic models/schemas
│   ├── __init__.py
│   ├── initial_data.py           # Initial data setup
│   └── main.py                   # FastAPI application
├── .env.example                  # Example environment variables
├── .gitignore
├── README.md
├── requirements.txt              # Project dependencies
└── start.sh                     # Development server script
```

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

This project uses Black for code formatting:

```bash
pip install black
black .
```

### Linting

This project uses flake8 for linting:

```bash
pip install flake8
flake8
```

## Deployment

For production deployment, consider using:

- Gunicorn or Uvicorn with multiple workers
- A reverse proxy like Nginx
- Process manager like systemd or Supervisor
- Environment variables for configuration
- Proper logging and monitoring

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [SQLAlchemy](https://www.sqlalchemy.org/) - The ORM used
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [Alembic](https://alembic.sqlalchemy.org/) - Database migrations draftline-api
DraftLine Backend APIs
