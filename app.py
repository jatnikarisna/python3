from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! Please wath The Pursuit now :)"

if __name__ == "__main__":
    app.run(host='0.0.0.0')