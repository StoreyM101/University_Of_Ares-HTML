import os
from flask import Flask, render_template, request, redirect, url_for, session # Imports the Python module known as Flask - a micro web development framework.

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Defines a key needed for efficient session handling.

# Defines the Data Dictionary when Ares-University-Dashboard.css appears on screen.
ares_user_info = { # Used to simulate a real database.
    "djohnny@gmail.com": { # Email field
        "password": "mathislife01", # password field
        "name": "John Doe", # Name of user field
        "lecturers": [ # Dictionary holding information used inside the table
            {"Lecturer": "Garry Lees", "Subject": "Algebra", "Email": "garry.lees@gmail.com", "Hours": "9AM-5PM"},
            {"Lecturer": "Jayne Warner", "Subject": "Arithmetic", "Email": "jayne.warner@gmail.com", "Hours": "12PM-6PM"},
            {"Lecturer": "Moira Cope", "Subject": "Trigonometry", "Email": "moira.cope@gmail.com", "Hours": "9AM-5PM"},
            {"Lecturer": "James Aspinall", "Subject": "Geometry", "Email": "j.aspinall@gmail.com", "Hours": "9AM-5PM"},
            {"Lecturer": "Winston Bannister", "Subject": "Number Theory", "Email": "winston.b@gmail.com", "Hours": "12PM-6PM"},
            {"Lecturer": "Kay Andrews", "Subject": "Probability", "Email": "kay.andrews@gmail.com", "Hours": "12PM-6PM"},
            {"Lecturer": "Mildred Goodall", "Subject": "Discrete Maths", "Email": "m.goodall@gmail.com", "Hours": "9AM-5PM"}
        ]
    }
}

#_____________________________________________________________First Route (Login)_____________________________________________________________

@app.route("/", methods=["GET", "POST"]) # Defines the route for the Login page. Allows for HTTP GET and POST methods.

def login(): # Defines Login function
    if request.method == "POST": # If the request method is a HTTP POST request, it means that the user submitted a form.
        email = request.form["email"] # Retrieves the entered email provided by user
        password = request.form["psword"] # Retrieves the entered password provided by user

        if email in ares_user_info and ares_user_info[email]["password"] == password: # if the entered username/password is found within the ares_user_info dictionary.
            session["email"] = email   # The email is stored within the session
            return redirect(url_for("dashboard"))  # User is redirected to dashboard
        else:  # if the entered email/password is not found within the ares_user_info dictionary.
            return "Invalid credentials, please try again.", 401 # Present error 401 (Unauthorised client error response)

    return render_template("Ares_Login.html")  # Displays login form using GET request.

#_____________________________________________________________Second Route (University Dashboard)_____________________________________________________________

@app.route("/dashboard") # Defines the route for the Dashboard page.

def dashboard(): # Defines dashboard function
    if "email" not in session: # If username is not logged in the session
        return redirect(url_for("login"))  # Redirects back to login page

    user_data = ares_user_info.get(session["email"]) # Retrieves user data from Dictionary
    if user_data: # If Data exists the move to next line
        return render_template("Ares_Dashboard.html", user=user_data) # Passes user data to Dashboard
    else: # If Data does not exist for user
        return redirect(url_for("login"))  # Redirects back to login if user not found

#_____________________________________________________________Third Route (Logout)_____________________________________________________________

@app.route("/logout", methods=["POST"]) # Defines the route for when a user logs out. Allows for HTTP POST (used for resource creation) method.

def logout(): # Defines function for logging out of Dashboard
    session.pop("email", None) # Remove user from session
    return redirect(url_for("login")) # Redirects users back to login screen 

if __name__ == "__main__": # ensures script runs only when executed directly
    app.run(debug=True) # enables auto-reload on code changes
