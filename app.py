from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/')
def hello():
    return 'Hello, world!'


@app.route('/api/v1/test1')
def test():
    return 'code change to test pipeline build'


@app.route('/api/v1/test2')
def test():
    return 'code change to test pipeline build'


if __name__ == '__main__':
    app.run()
