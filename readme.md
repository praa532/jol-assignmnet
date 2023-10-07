# FastAPI Backend Project README

This FastAPI backend project provides a sample implementation of an authentication system using PostgreSQL (PSQL) for user data and a Redis-like in-memory database for caching. It includes versioned endpoints and demonstrates how to handle user authentication, update user information, and retrieve user data.

# Project Structure
The project structure follows the following directory hierarchy:

project_root/
  ├── app/
  │    ├── __init__.py
  │    ├── main.py
  │    ├── endpoints/
  │    │    ├── __init__.py
  │    │    ├── auth.py
  │    │    ├── user.py
  │    ├── models.py
  │    ├── utils/database/redis
  │    │    ├── __init__.py
  │    │    ├── psql.py
  │    │    ├── redis.py
  ├── requirements.txt
  
app/: Contains the main application code.
app/main.py: Configures the FastAPI app and mounts endpoints.
app/endpoints/: Contains API endpoints, including authentication and user-related endpoints.
app/models.py: Defines data models for the application.
app/utils/: Houses utility modules for database and Redis connections.
requirements.txt: Lists project dependencies.

# Database Setup
This project uses PostgreSQL for user data storage. Make sure to create a PostgreSQL database and configure the connection URL in utils/database.py. You can create the users table as described in the README or customize it according to your requirements.

# Redis 
A Redis-like in-memory cache is used for session management and data caching. Configure the Redis connection in utils/redis_cache.py. Ensure that you have a running Redis server to store session data.

# Authentication
The /login endpoint in endpoints/auth.py performs user authentication using PostgreSQL. It checks if the provided credentials (username and password) match the database records. If authentication is successful, it generates a JSON Web Token (JWT) for the user and returns it as an access token.

# User Operations
/setName: This endpoint allows authenticated users to update their name in the database. It requires a valid authorization token in the header.
/getName: Authenticated users can retrieve their name from the database using this endpoint. It also requires a valid authorization token.

# Running the Application
You can run the application using Uvicorn or Gunicorn:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000

or

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app -b 0.0.0.0:8000

Ensure you have installed the required packages listed in requirements.txt.

# Security

Make sure to secure your application by using secure secret keys for JWT token encoding and by following best practices for authentication and authorization.

# Customization

Feel free to customize this project to suit your specific requirements. You can add more endpoints, enhance authentication mechanisms, or integrate other features as needed.