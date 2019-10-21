from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from rapyuta.io, I can edit and rebuild with the git flow"


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
