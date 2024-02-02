from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import logging


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site_status.db'
db = SQLAlchemy(app)

# Define the database model for WebsiteStatus
class WebsiteStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(255), nullable=False)
    status_code = db.Column(db.Integer, nullable=True)

# List of websites to check
WEBSITES = [
    {'name': 'Amazon', 'url': 'https://www.amazon.com'},
    {'name': 'Flipkart', 'url': 'https://www.flipkart.com'},
    {'name': 'Zomato', 'url': 'https://www.zomato.com'},
    {'name': 'Swiggy', 'url': 'https://www.swiggy.com'},
    {'name': 'LinkedIn', 'url': 'https://www.linkedin.com'},
    {'name': 'Google', 'url': 'https://www.google.com'},
    {'name': 'Youtube', 'url': 'https://www.youtube.com/'},
    {'name': 'GitHub', 'url': 'https://www.github.com'},
    {'name': 'Example error 1', 'url': 'https://www.example3.com/forbidden-page'},
    {'name': 'Example error 2', 'url': 'https://www.example1.com/nonexistent-page'},
]

# Configure the logger
logging.basicConfig(filename='app.log', level=logging.INFO)

# Create tables before the first request
with app.app_context():
    db.create_all()

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html', websites=WEBSITES)

# Route to check the status of a website (POST request)
@app.route('/check_status', methods=['POST'])
def check_status():
    # Get JSON data from the request
    data = request.get_json()
    website_name = data.get('website_name', '').lower()

    # Find the matching website in the predefined list
    matching_website = next((site for site in WEBSITES if website_name in site['name'].lower()), None)

    if not matching_website:
        # Return an error if the website is not found in the list
        return jsonify({'error': 'Enter a correct website name from the list'})

    try:
        # Get the status code using the get_status_code function
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
        status_code = get_status_code(matching_website['url'], headers=headers)
        app.logger.info(f"Status code for {matching_website['url']}: {status_code}")
    except Exception as e:
        # Log an error if there is an exception while checking the status
        app.logger.error(f"Error checking status for {matching_website['url']}: {e}")
        return jsonify({'error': f"Error checking status for {matching_website['url']}: {e}"}), 500

    # Add the new status to the database
    new_status = WebsiteStatus(website=matching_website['url'], status_code=status_code)
    db.session.add(new_status)
    db.session.commit()

    # Return the status code as JSON response
    return jsonify({'status': status_code})

# Function to get the status code of a website using requests
def get_status_code(website, headers=None):
    try:
        response = requests.get(website, headers=headers, timeout=5, allow_redirects=True)
        return response.status_code  # Return the actual status code even if it's not 2xx
    except requests.RequestException as e:
        # Log an error if there is an exception while making the request
        app.logger.error(f"Error checking status for {website}: {e}")
        return 0  # Represents an error

if __name__ == '__main__':
    app.run(debug=True)
