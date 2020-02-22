from flask import render_template

from deliberate_spending import app

@app.route('/')
def index():
  return render_template('index.html')
