from flask import Flask
app = Flask('MaratonaScrapping')

@app.route('/')
def hello_world():
    return 'Hello, world!!!'

@app.route('/login')
def login():
    return 'Pagina de login'

app.run(host='0.0.0.0')
