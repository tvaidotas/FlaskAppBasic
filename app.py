from flask import Flask

# Comment from Andrew...
# Another comment...

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello everyone !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

@app.route('/xyz')
def xyz():
    return 'Hello from XYZ'

if __name__ == '__main__':
    app.run()
