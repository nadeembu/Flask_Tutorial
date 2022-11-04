# Youtube video link:
# https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
# Learn Adding Navbar Bootstrap and HTML file inheritance


from flask import Flask, render_template

# Create an instance for our Flask applicationMain
app = Flask(__name__)


@app.route("/")
# app.route defines the path to our webpages
def home():
    # Render the index.html page.
    return render_template("index.html")


@app.route("/<name>")
# app.route defines the path to our webpages
def users(name):
    # Render the index.html page. Pass the value of the "content" variable to
    # index.html. Pass multiple variables in a list:
    # ["Nadeem", "Tim", "Susan"])
    return render_template("index tutorial 3.html", content=["Nadeem", "Tim", "Susan", "Frank", "Grant"])


if __name__ == "__main__":
    # debug=True will run the web server every time you save a file.
    # Saves you having to stop/start it each time!
    app.run(debug=True)
