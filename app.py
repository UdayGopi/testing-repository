from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Retrieve the commit SHA from environment variable, default to 'unknown'
    commit_sha = os.environ.get('COMMIT_SHA', 'unknown')
    # Display the first 7 characters of the commit SHA
    return f"Hello, World! I am running from commit: {commit_sha[:7]}\n"

if __name__ == '__main__':
    # Run the Flask app on all available network interfaces on port 5000
    app.run(host='0.0.0.0', port=5000)