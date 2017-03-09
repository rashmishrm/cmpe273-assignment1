from flask import Flask
from github import Github

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.rout("/v1/<filename>")
def getFile(filename):


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
