from flask import Flask, render_template
from database import load_gesla

app = Flask(__name__)


@app.route('/')
def index():
    podatki = load_gesla()
    return render_template('home.html', podatki=podatki)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
