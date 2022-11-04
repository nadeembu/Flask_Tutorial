# Youtube video link:
# https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
# Learn about sessions


from flask import Flask, render_template, request, redirect, url_for, session
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
        return redirect(url_for("user"))
    else:
        # Check if user already logged in. If so, redirect to user page.
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")


@app.route("/logout")
def logout():
    # Remove "user" from the session dictionary to clear session
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/user")
def user():
    # Check if user logged in by checking session information
    if "user" in session:
        # Get the user data
        user = session["user"]
        return f"<h1> {user} is being displayed by the user function <h1>"
    else:
        # If no user in session information. Redirect to login function
        return redirect(url_for("login"))


@app.route("/<name>")
def users(name):
    return render_template("index tutorial 3.html", content=["Nadeem", "Tim", "Susan", "Frank"])


if __name__ == "__main__":
    app.run(debug=True)
