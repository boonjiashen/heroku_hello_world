import os
from flask import Flask

default_port = 5000
default_host = '0.0.0.0'

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":

    # Get app parameters
    port = int(os.environ['PORT'])  \
            if 'PORT' in os.environ  \
            else default_port

    # Print default status
    if 'PORT' not in os.environ:
        print('No environment variable PORT, defaulting to port=%i'  %
                default_port)

    # Run app
    kwargs = {'host':default_host, 'port':port}
    app.run(**kwargs)
