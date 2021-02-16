from flask import Flask, render_template, request

app = Flask('MaratonaScrapping')

@app.route('/')
def hello_world():
    return 'Hello, world!!!'

'''
@app.route('/<user>')
def user(user):
    return f'oi, bem vindo {user}'
'''

@app.route('/search')
def search():
  return render_template('search.html')

@app.route('/result')
def result():
  keyword = request.args.get('keyword')
  return render_template('result.html', keyword=keyword)

app.run(host='0.0.0.0')
