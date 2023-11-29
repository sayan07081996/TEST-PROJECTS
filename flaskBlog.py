from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return "<h1>Testing Diff IP'S</h1>"

@app.route("/about")
def about_page():
    return "<h1>About Page in Mozilla</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)
    # app.run()
