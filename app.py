from flask import Flask
from github import Github
import sys
import json
import yaml

git_repo=''

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/<name>")
def getConfig(name):
    client = Github()
    repo = client.get_repo(git_repo);
    file_content = repo.get_file_contents(removeExtension(name)+'.yml');
    return getOutput(str(name),file_content.decoded_content);

def removeExtension(name):
    return name.split('.')[0];

def getOutput(fileName,content):
    if  fileName.endswith('.yml'):
        return content
    elif fileName.endswith('.json'):
        return json.dumps(yaml.load(content), sort_keys=False, indent=2)


if __name__ == "__main__":
    for arg in sys.argv: 1
    print arg
    git_repo = arg.replace('https://github.com/','')
    app.run(debug=True,host='0.0.0.0')
