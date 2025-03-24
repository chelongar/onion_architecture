# Onion Architecture + Domain-Driven Design

A clean, maintainable ToDo API built with **FastAPI**, structured using **Onion Architecture**, and guided by **Domain-Driven Design** (DDD). Designed for clarity, separation of concerns, and long-term scalability.

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
## 🚀 Features
```yaml

- ✅ RESTful ToDo API built with FastAPI
- ✅ Domain-first design using DDD
- ✅ Onion architecture layering
- ✅ Validated input with Pydantic
- ✅ Deadline support with timezone-aware datetime
- ✅ Dockerized for easy deployment
```

## 📦 Project Structure
- onion_architecture 
    - domain/ # Core business logic (entities, value objects, interfaces)
      - entities.py
      - repositories.py
    - application/ # Application services (use cases)
    - infrastructure/ # Repositories, API, external concerns 
      - in_memory_repo.py
    - main.py # FastAPI entry point
    - requirements.txt # Python dependencies 
    - Dockerfile # Container build config
    - docker-compose.yml # Container orchestration
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

