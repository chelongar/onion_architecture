# Onion Architecture + Domain-Driven Design

A clean, maintainable ToDo application built with **Domain-Driven Design (DDD)** and **Onion Architecture**.  
Powered by **FastAPI**, **PostgreSQL**, and **Docker** for modern, async, containerized development.
---

## 📐 Architecture Overview

This project follows the **Onion Architecture** with clear Domain-Driven Design boundaries:

```less
           [ Infrastructure Layer ]
                  | FastAPI
                  | InMemory Repository
                  ↓
          [ Application Layer ]
                | Use Cases
                ↓
          [ Domain Layer ]
        | Entities, Value Objects, Interfaces
```
## 🚀 Technology Stack
```yaml

✅ Python 3.11
✅ FastAPI — Async Web API
✅ PostgreSQ
✅ SQLAlchemy + databases
✅ Docker & Docker Compose
✅ Onion Architecture
✅ DDD Principles

```

## 📦 Project Structure
- onion_architecture 
    - domain/
      - entities.py
      - repositories.py
    - application/
    - infrastructure/
      - postgresql_repo.py
    - main.py
    - requirements.txt
    - Dockerfile
    - docker-compose.yml
    - LICENSE

## ⚙️ Requirements
```yaml
- Python 3.11+
- Docker & Docker Compose
```

## 🐳 Getting Started (Docker)
```bash
# Build and run the app
docker-compose up --build
```

### Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🤝 Contributing
Pull requests welcome!

