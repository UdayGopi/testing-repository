from flask import Flask, request, jsonify
import json

# Create a Flask application instance
app = Flask(__name__)

# Define a route that listens for POST requests on '/webhook'
@app.route('/webhook', methods=['POST'])
def github_webhook():
    # Check if the request has JSON data
    if request.is_json:
        payload = request.get_json()

        # Print the event type from the GitHub header
        event_type = request.headers.get('X-GitHub-Event')
        print(f"Received '{event_type}' event.")

        # Print some information from the payload
        if 'pusher' in payload:
            print(f"Pushed by: {payload['pusher']['name']}")
        if 'repository' in payload:
            print(f"Repository: {payload['repository']['full_name']}")

        # In the future, you will trigger your CI/CD pipeline here

        return jsonify({"status": "success", "message": "Webhook received"}), 200
    else:
        return jsonify({"status": "error", "message": "Request was not JSON"}), 400

# Main entry point to run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)