import os
from flask import Flask, render_template

app = Flask(__name__)

geslo = 'sila'
opis = 'sila je moja najljubša igra'

from sqlalchemy import create_engine, text

connection_string = os.getenv('GRAFIS_PG_CONN_STR')
print(connection_string)

# Database
engine = create_engine(connection_string)



with engine.connect() as conn:
    result = conn.execute(text('select * from slovar'))
    podatki = list(result.all())

@app.route('/')
def index():
    return render_template('home.html', geslo=geslo, opis=opis, podatki=podatki)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
