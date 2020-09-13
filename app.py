from flask import Flask

#creating a new Flask instance
app = Flask(__name__)

#Adding root and creating function hello world
@app.route('/')
def hello_world():
    return 'Hello world'