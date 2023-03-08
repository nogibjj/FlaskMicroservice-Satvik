from flask import Flask
from flask import request
import os


global_store = ["unknown"]

app = Flask(__name__)
@app.route("/")
def hello():
    return "Welcome to Flask, have fun!"


@app.route("/input")
def opt1():
    user = request.args.get("user")
    # global_store[0] = user
    return f"User is {user}"


@app.route("/output")
def opt2():
    return f"User is {global_store[0]}"


@app.route("/square")
def opt3(n=None):
    if n is None:
        n = request.args.get("n")
        n = int(n)
    # global_store[0] = user
    return str(n**2)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    