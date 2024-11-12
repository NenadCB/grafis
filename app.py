from flask import Flask, render_template, request
from database import load_gesla

app = Flask(__name__)


@app.route('/')
def index():
    podatki = {}
    iskalnik = request.args
    
    if 'q' in iskalnik:
        if iskalnik['q'] != '':
            podatki = load_gesla(iskalnik)

    return render_template('home.html', podatki=podatki)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
