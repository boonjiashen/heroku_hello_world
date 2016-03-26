from flask import Flask

DEFAULT_PORT = 5000
DEFAULT_HOST = '0.0.0.0'

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    kwargs = {'host':DEFAULT_HOST, 'port':DEFAULT_PORT}
    app.run(**kwargs)
