import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, world!!! <i>(Irina)</i></h1>'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port)