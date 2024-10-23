from flask import Flask, render_template

app = Flask(__name__)

geslo = 'sila'
opis = 'sila je moja najljubša igra'


@app.route('/')
def index():
    return render_template('home.html', geslo=geslo, opis=opis)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
