# transport-ticketing-api

## Project Idea
A backend system for an online transport ticketing platform where users can search for available trips, book tickets, and manage their bookings. Transport companies (admins) can add and manage routes, trips, and seat availability.
## Features
-User registration and login (passengers and admins)

-Admins can create transport companies, routes, and trips

-Passengers can search available trips by date, origin, and destination

-Ticket booking system with seat availability

-Booking history for users

-Basic admin dashboard for managing trips and bookings

## Backend Models
User (customized) =  [username, email, password, role(admin, passenger)]

TransportCompany = [name,owner(FK to User), contact info]

Route = [origin, destination, duration estimate]

Trip = [route(FK to route), transport company(FK), departure time, available seats, price]

Booking = [trip (FK to Trip), user (FK to User), seats_booked, booking_time, status (confirmed, cancelled)]

## API Endpoints
#GET Requests

/api/routes/ = View all routes

/api/routes/<id>/ = View a specific route

/api/trips/ = View all trips

/api/trips/<id>/ = View a specific trip

/api/bookings/ = View your bookings (user only)

/api/company/bookings/ = View all bookings for your company (admin only)

/api/transport-companies/ = View all transport companies

/api/profile/ = View your user profile

#POST Requests

/api/register/ = Register a new user

/api/login/ = Log in and get authentication token

/api/routes/ = Create a new route (admin only)

/api/trips/ = Create a new trip (admin only)

/api/bookings/ = Make a booking (user only)

/api/transport-companies/ = Create a new transport company (admin only)

#PUT / PATCH Requests

/api/routes/<id>/ = Update a route (admin only)

/api/trips/<id>/ = Update a trip (admin only)

#DELETE Requests

/api/routes/<id>/ = Delete a route (admin only)

/api/trips/<id>/ = Delete a trip (admin only)
