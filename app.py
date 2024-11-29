from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages

# Dummy user data for demonstration purposes
users = {'user@example.com': 'password'}  # Replace this with a real user database

@app.route('/')
def home():
    return render_template('index.html')  # Render the main index.html

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Check if the email and password match the dummy user data
    if email in users and users[email] == password:
        flash('Login successful!', 'success')  # Flash success message
        return redirect(url_for('home'))  # Redirect to home page after successful login
    else:
        flash('Invalid credentials. Please try again.', 'danger')  # Flash error message
        return redirect(url_for('home'))  # Redirect back to home page

@app.route('/about')
def about():
    return render_template('index1.html')  # Render the about section (you can create a separate template if needed)

@app.route('/menu')
def menu():
    return render_template('index1.html')  # Render the menu section (you can create a separate template if needed)

@app.route('/specials')
def specials():
    return render_template('index1.html')  # Render the specials section (you can create a separate template if needed)

@app.route('/events')
def events():
    return render_template('index1.html')  # Render the events section (you can create a separate template if needed)

@app.route('/chefs')
def chefs():
    return render_template('index1.html')  # Render the chefs section (you can create a separate template if needed)

@app.route('/gallery')
def gallery():
    return render_template('index1.html')  # Render the gallery section (you can create a separate template if needed)

@app.route('/contact')
def contact():
    return render_template('index1.html')  # Render the contact section (you can create a separate template if needed)

if __name__ == '__main__':
    app.run(debug=True)