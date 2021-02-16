from flask import Flask, render_template, request, redirect
from day_08.scrapping import get_jobs

app = Flask('MaratonaScrapping')

@app.route('/')
def hello_world():
    return 'Olá mundo '

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
  if keyword:
    search_result = get_jobs(keyword)
  else:
    return redirect('/')
  return render_template('result.html', keyword=keyword, jobs=search_result)


app.run(host='0.0.0.0')
