from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def index():
    return "Service is running!"

if __name__ == '__main__':
    print("Flask app is running! Access it at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)