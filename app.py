from flask import Flask

# Comment from Andrew...

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello everyone !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

@app.route('/abc')
def abc():
    return 'Hello from ABC'

if __name__ == '__main__':
    app.run()
