# Event Management System

## Overview
The **Event Management System** is a web-based application built using Django Rest Framework (DRF) that allows users to create, manage, and book events. It provides authentication, event listings, bookings, and notifications for a seamless event management experience.

## Features
- **User Authentication**: Registration, login, and JWT-based authentication.
- **Event Management**: Create, update, and delete events.
- **Event Booking**: Users can book available events.
- **Admin Dashboard**: Admins can manage users, events, and bookings.
- **Email Notifications**: Automated emails for event bookings and confirmations.
- **Payment Integration**: Supports Paystack for event payments.

## Technologies Used
- **Backend**: Django Rest Framework (DRF)
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: PostgreSQL
- **Payment Gateway**: Paystack
- **Task Queue**: Celery with Redis (for async tasks like email notifications)

## Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/Event-management-system.git
   cd event-management-system
   ```

2. **Create a virtual environment and activate it**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (Create a `.env` file and add your credentials)
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/event_db
   PAYSTACK_SECRET_KEY=your_paystack_secret_key
   ```

5. **Apply database migrations**
   ```sh
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```sh
   python manage.py runserver
   ```

## API Endpoints
| Method | Endpoint | Description |
|--------|-------------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and get JWT token |
| GET | `/api/events/` | List all events |
| POST | `/api/events/create/` | Create a new event (Admin only) |
| GET | `/api/events/<id>/` | Get event details |
| POST | `/api/bookings/` | Book an event |
| GET | `/api/bookings/user/` | View user bookings |

## Running Tests
To run tests, execute:
```sh
pytest
```

## Deployment
For deployment, configure Gunicorn and Nginx, or deploy using platforms like **Heroku**, **DigitalOcean**, or **AWS**.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, contact **chisomzzy1@gmail.com**.

