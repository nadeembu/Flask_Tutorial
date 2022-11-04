# Youtube video link:
# https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
# Learn HTTP Methods GET and POST


from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get the username that was entered from the input in login.html
        # Store that value as a dictionary and assign it to the variable "user"
        user = request.form["username"]
        # Redirect to the user function and pass it the variable "user".
        return redirect(url_for("user", usr=user))
    else:
        # Condition met if anything other than a "POST" request.
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1> {usr} is being displayed by the user function <h1>"
    # return render_template("user.html")


@app.route("/<name>")
def users(name):
    return render_template("index tutorial 3.html", content=["Nadeem", "Tim", "Susan", "Frank"])


if __name__ == "__main__":
    app.run(debug=True)
