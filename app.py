from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Digital Barry says HELLO!'})

@app.route('/api/user/<name>', methods=['GET'])
def user(name):
    return f"Welcome, {escape(name)}"  # Potential XSS vulnerability

import os

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)