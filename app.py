import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Updated fake_users with structured transactions
fake_users = {
    "djohnny@gmail.com": {
        "password": "mathislife01",
        "name": "John Doe",
        "lecturers": [
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

# ________________ Login Route ________________
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["psw"]

        if email in fake_users and fake_users[email]["password"] == password:
            session["email"] = email  
            return redirect(url_for("dashboard"))  
        else:
            return "Invalid credentials, please try again.", 401  

    return render_template("Login.html")  

# ________________ Dashboard Route ________________
@app.route("/dashboard")
def dashboard():
    if "email" not in session:
        return redirect(url_for("login"))  

    user_data = fake_users.get(session["email"])
    if user_data:
        return render_template("Dashboard.html", user=user_data)  
    else:
        return redirect(url_for("login"))  

# ________________ Logout Route ________________
@app.route("/logout", methods=["POST"])
def logout():
    session.pop("email", None)  
    return redirect(url_for("login"))  

if __name__ == "__main__":
    app.run(debug=True)
