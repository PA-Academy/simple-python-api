from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Digital Barry says HELLO!'})

@app.route('/api/user/<name>', methods=['GET'])
def user(name):
    return f"Welcome, {escape(name)}"  # Potential XSS vulnerability

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)