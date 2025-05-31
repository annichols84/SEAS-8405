from flask import Flask, request, jsonify, redirect
import jwt

app = Flask(__name__)

@app.route("/")
def index():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing token"}), 401
    token = auth_header.split()[1]
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return jsonify({"message": "Welcome!", "user": decoded})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/login")
def login():
    return redirect(
        "http://localhost:8080/realms/FintechApp/protocol/openid-connect/auth"
        "?client_id=flask-client"
        "&response_type=code"
        "&redirect_uri=http://localhost:15000/login/callback"
    )

@app.route("/login/callback")
def login_callback():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "Missing authorization code"}), 400

    return jsonify({"message": "Login successful!", "code": code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
