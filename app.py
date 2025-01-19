from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Path to the JSON file
USER_CREDENTIALS_FILE = 'user_credentials.json'

# Load user credentials from JSON file
def load_user_credentials():
    if os.path.exists(USER_CREDENTIALS_FILE):
        with open(USER_CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save user credentials to JSON file
def save_user_credentials(credentials):
    with open(USER_CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file)

# Initialize user credentials
USER_CREDENTIALS = load_user_credentials()

@app.route('/')
def home():
    return render_template('Welcome.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            return render_template('Welcome2.html', username=username)
        else:
            return render_template('Error.html', username=username)
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USER_CREDENTIALS:
            return render_template('Error2.html', username=username)
        else:
            USER_CREDENTIALS[username] = password
            save_user_credentials(USER_CREDENTIALS)
            return render_template('Registered.html', username=username)
    return render_template('signup.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']
        if username in USER_CREDENTIALS:
            USER_CREDENTIALS[username] = new_password
            save_user_credentials(USER_CREDENTIALS)
            return redirect(url_for('signin'))  # Redirect to the signin page
        else:
            return render_template('error1.html', message="Username not found.")
    return render_template('forgot_password.html')

# Route for the "Create Yearbook" page
@app.route('/create_yearbook', methods=['GET', 'POST'])
def create_yearbook():
    if request.method == 'POST':
        # Handle the data submitted by the user here
        template = request.form.get('template')
        photos = request.files.getlist('photos')
        monthly_text = request.form.get('monthly_text').split(',')

        # Process the yearbook creation logic (e.g., save data, generate yearbook, etc.)
        # For now, we'll just simulate a successful creation
        return render_template('YearbookCreated.html', template=template)

    return render_template('create_yearbook.html')

if __name__ == '__main__':
    app.run(debug=True)
