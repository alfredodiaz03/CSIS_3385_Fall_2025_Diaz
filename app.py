from flask import Flask, jsonify, request
import json, time

app = Flask(__name__)

# Load pre-seeded users from JSON file
with open('seed.json', 'r') as f:
    users = json.load(f)

# -------------------------------
# CRUD SNIPPETS WILL BE INSERTED HERE
# -------------------------------
# --------------------
# GET (read all users)
# --------------------
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# ------------------------------------------------------
# POST (create) — form uses odd keys -> normalize fields
# doggy -> username, zebra42 -> password,
# kittycat -> email, rocketShip -> age
# ------------------------------------------------------
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    username = data.get('doggy')
    password = data.get('zebra42')
    email = data.get('kittycat')
    age = data.get('rocketShip')

    # Build id with a short timestamp suffix (simple uniq-ish id)
    timestamp = str(int(time.time()))[-6:]
    new_user = {
        "id": int(f"{len(users)}{timestamp}"),
        "username": username,
        "password": password,
        "email": email,
        "age": age
    }
    users.append(new_user)
    return jsonify(new_user), 201

# ------------------------------------------------------
# PUT (update by id) — expects *normalized* keys in body
# ------------------------------------------------------
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json() or {}
    for user in users:
        if user['id'] == user_id:
            user['username'] = data.get('username', user['username'])
            user['email']    = data.get('email',    user['email'])
            user['age']      = data.get('age',      user['age'])
            user['password'] = data.get('password', user['password'])
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# -----------------------------
# DELETE (remove by id)
# -----------------------------
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": f"User {user_id} deleted"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
