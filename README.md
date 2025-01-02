# FastAPI Project with JWT Authentication, Redis, and Celery

This project implements a FastAPI application with JWT-based authentication, Redis for caching, and Celery for background tasks.

## Features
- **RESTful API** for managing users, bookings, hotels, and rooms.
- **JWT Authentication** for secure access control.
- **Redis Caching** for efficient data retrieval.
- **Celery** for asynchronous task processing.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start Redis server:
   ```bash
   docker run -p 6379:6379 redis
   ```

3. Start FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

4. Start Celery worker:
   ```bash
   celery -A app.celery worker
   ```

## Endpoints

- **Users**: Manage users and authenticate using JWT.
- **Bookings**: CRUD operations for bookings.
- **Hotels**: Manage hotel data.
- **Rooms**: Manage room details.

## Admin Interface

- Admin panel available for managing users, bookings, hotels, and rooms.

## License
This project is licensed under the MIT License.
