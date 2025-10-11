# Project 2 – Flask Puzzle Server
Author: Alfredo Diaz  
Course: CSIS 3385 – Database and Web Vulnerability and Security  

## Overview
This project is a Flask API built from code snippets that I had to piece together like a puzzle. The goal was to connect an HTML form (that had no documentation) to a working backend server using the correct CRUD operations — Create, Read, Update, and Delete.

I analyzed how the form sent data, figured out the field names it used, and then matched the correct backend code for each route. After building it, I ran everything in Docker and tested it with PowerShell.

## Features
- **GET /users** – Returns a list of users in JSON format  
- **POST /users** – Creates a new user using these mapped fields:  
  - doggy → username  
  - zebra42 → password  
  - kittycat → email  
  - rocketShip → age  
- **PUT /users/<id>** – Updates an existing user by ID  
- **DELETE /users/<id>** – Deletes a user by ID  

All routes return the proper HTTP status codes (200, 201, 404).

## Snippet Verification
For this project, I had to choose one correct snippet from each CRUD section. Below is what I used and why:

- **GET:**  
  I used `@app.route('/users', methods=['GET'])` that returns `jsonify(users), 200`.  
  It’s the correct route and response since 200 means success.

- **POST:**  
  I used the version that takes the special form keys (`doggy`, `zebra42`, `kittycat`, `rocketShip`) and maps them to normal field names.  
  It also adds a timestamp for a unique ID and returns a 201 “Created” response.

- **PUT:**  
  I used `@app.route('/users/<int:user_id>', methods=['PUT'])`.  
  This one properly updates the user’s info based on the given ID and returns 200 if successful or 404 if not found.

- **DELETE:**  
  I used `@app.route('/users/<int:user_id>', methods=['DELETE'])`.  
  It finds the user by ID, removes them from the list, and gives a 200 confirmation or 404 if they don’t exist.

Each of these choices matched the clues from the HTML form and followed the correct RESTful structure.

## Notes
- The app runs on Docker and automatically reloads seed data from `seed.json` each time the container restarts.  
- Each CRUD route works individually and matches the snippets from the project instructions.  
- Data resets after each container restart (expected behavior).

## Summary
This assignment helped me understand how Flask routes connect the frontend to the backend and how each CRUD operation works in practice.  
It also helped me see how important correct HTTP methods and status codes are when designing secure and functional APIs.
