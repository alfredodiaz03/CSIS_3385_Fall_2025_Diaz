# Project 2 – Flask Puzzle Server
Author: Alfredo Diaz
Course: CSIS 3385 – Database and Web Vulnerability and Security

Overview
This project is a Flask API built from code snippets that I had to piece together like a puzzle. The goal was to connect an HTML form (that had no documentation) to a working backend server using the correct CRUD operations — Create, Read, Update, and Delete.

I analyzed how the form sent data, figured out the field names it used, and then matched the correct backend code for each route. After building it, I ran everything in Docker and tested it with PowerShell.

Features
- GET /users – Returns a list of users in JSON format
- POST /users – Creates a new user using these mapped fields:
  - doggy → username
  - zebra42 → password
  - kittycat → email
  - rocketShip → age
- PUT /users/<id> – Updates an existing user by ID
- DELETE /users/<id> – Deletes a user by ID

All routes return the proper HTTP status codes (200, 201, 404).

How to Run
docker build -t flask-puzzle-server .
docker run -p 5001:5000 flask-puzzle-server

How to Test (PowerShell)
# Read (GET)
irm http://localhost:5001/users

# Create (POST)
irm http://localhost:5001/users -Method Post -ContentType 'application/json' -Body '{"doggy":"neo","zebra42":"tr1n1ty!","kittycat":"neo@example.com","rocketShip":29}'

# Update (PUT)
irm http://localhost:5001/users/2221899 -Method Put -ContentType 'application/json' -Body '{"email":"one@example.com","age":30}'

# Delete (DELETE)
irm http://localhost:5001/users/2221899 -Method Delete

Notes
- The app runs on Docker and automatically reloads seed data from seed.json each time the container restarts.
- Each CRUD route works individually and matches the snippets from the project instructions.
- Data resets after each container restart (expected behavior).

Summary
This assignment helped me understand how Flask routes connect the frontend to the backend and how each CRUD operation works in practice. It also showed me how to test endpoints safely and interpret JSON responses from an API.
```
