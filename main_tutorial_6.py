# Youtube video link:
# https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
# Learn Message flashing tutorial


from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta


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
        # Enable permanent session
        session.permanent = True
        user = request.form["username"]
        # Setup session data based on what the user typed in.
        # Session stores ["user"] data as a dictionary.
        session["user"] = user
        flash("Login successful")
        return redirect(url_for("user"))
    else:
        # Check if user already logged in. If so, redirect to user page.
        if "user" in session:
            flash("Redirected back to the user page. As wou were already logged in")
            return redirect(url_for("user"))
        else:
            return render_template("login.html")


@app.route("/logout")
def logout():
    # Check if you were logged in.
    if "user" in session:
        user = session["user"]
        flash("You've been logged out", "info")
    # Remove "user" from the session dictionary to clear session data
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/user")
def user():
    # Check if user logged in by checking session information
    if "user" in session:
        # Get the user data
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))


@app.route("/<name>")
def users(name):
    return render_template("index tutorial 3.html", content=["Nadeem", "Tim", "Susan", "Frank"])


if __name__ == "__main__":
    app.run(debug=True)
