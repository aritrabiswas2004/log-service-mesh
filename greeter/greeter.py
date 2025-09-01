from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    return f"Hello from version 2", {'Content-Type': 'text/plain'} # change to version 1/2 when creating image

if __name__ == '__main__':
    app.run("0.0.0.0", port=9000)