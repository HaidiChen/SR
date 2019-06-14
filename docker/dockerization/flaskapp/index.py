from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    path = "./shared_folder"
    lists = os.listdir(path)
    return str(lists)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
