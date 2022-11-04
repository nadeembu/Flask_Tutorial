# Youtube video link:
# https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
# Learn Using SQLAlchemy Database


from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
# import sqlalchemy


app = Flask(__name__)

# Secret key needed to encrypt/decrypt the session data.
app.secret_key = "nadeemtest"

# Permanent session data stored for 5 days.
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        session["user"] = user
        flash("Login successful")
        return redirect(url_for("user"))
    else:
        # Check if user already logged in. If so, redirect to user page.
        if "user" in session:
            flash("Redirected back to the user page. As you were already logged in")
            return redirect(url_for("user"))
        else:
            return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You've been logged out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/user", methods=["GET", "POST"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Your email has been saved")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))


@app.route("/<name>")
def users(name):
    return render_template("index tutorial 3.html", content=["Nadeem", "Tim", "Susan", "Frank"])


if __name__ == "__main__":
    app.run(debug=True)
