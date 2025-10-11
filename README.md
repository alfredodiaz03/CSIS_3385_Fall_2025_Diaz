# Project 2 – Flask Puzzle Server
Author: Alfredo Diaz  
Course: CSIS 3385 – Database and Web Vulnerability and Security  
Instructor: Professor Hopper  

## Overview
This project was designed to test problem-solving and backend development skills by analyzing an undocumented HTML form and building a working Flask server. The goal was to match each CRUD operation (Create, Read, Update, Delete) with the correct code snippets and make the server function as expected. The project runs inside a Docker container and uses PowerShell for testing API routes.

## What the Server Does
- GET /users – Displays all existing users  
- POST /users – Creates a new user with form data (doggy, zebra42, kittycat, rocketShip) mapped to username, password, email, and age  
- PUT /users/<id> – Updates an existing user by their ID  
- DELETE /users/<id> – Deletes a user by their ID  

## Technologies Used
- Python 3.9  
- Flask 3.0.3  
- Docker  
- PowerShell (for testing)  

## Example PowerShell Commands
irm http://localhost:5001/users

irm http://localhost:5001/users -Method Post -ContentType 'application/json' -Body '{"doggy":"neo","zebra42":"tr1n1ty!","kittycat":"neo@example.com","rocketShip":29}'

irm http://localhost:5001/users/2221899 -Method Put -ContentType 'application/json' -Body '{"email":"one@example.com","age":30}'

irm http://localhost:5001/users/2221899 -Method Delete

## How to Run
docker build -t flask-puzzle-server .
docker run -p 5001:5000 flask-puzzle-server

## Notes
All CRUD routes return the correct HTTP status codes and follow secure handling practices.  
The project resets user data every time the container restarts, reloading from the seed.json file.  
This project demonstrates secure API design, testing with PowerShell, and proper use of Docker containers.
