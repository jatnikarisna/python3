from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! Please watch The Pursuit now 04th March 2025 9:50PM:)"

if __name__ == "__main__":
    app.run(host='0.0.0.0')