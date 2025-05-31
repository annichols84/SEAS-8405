from flask import Flask, jsonify, request

app = Flask(__name__)

# Security Enhancements:
# - Enforces strict request validation
# - Limits exposure by binding to localhost
# - Implements basic health check

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify service uptime."""
    return jsonify({"status": "healthy"}), 200

@app.route('/secure-data', methods=['POST'])
def secure_data():
    """Processes incoming data securely with validation."""
    data = request.get_json()
    if not data or "input" not in data:
        return jsonify({"error": "Invalid request"}), 400
    
    processed_data = {"message": f"Processed securely: {data['input']}"}
    return jsonify(processed_data), 200

if __name__ == '__main__':
    # Bind Flask service to localhost for security
    app.run(host='127.0.0.1', port=5000, debug=False)
