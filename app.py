from flask import Flask, render_template

app = Flask(__name__)

geslo = 'sila'
opis = 'sila je moja najljubša igra'

from sqlalchemy import create_engine, text

# Database
engine = create_engine("postgresql://grafis_owner:RTogb40WyXmG@ep-autumn-sunset-a8e3slx5.eastus2.azure.neon.tech/grafis?options=endpoint%3Dep-autumn-sunset-a8e3slx5"
)


with engine.connect() as conn:
    result = conn.execute(text('select * from slovar'))
    podatki = list(result.all())

@app.route('/')
def index():
    return render_template('home.html', geslo=geslo, opis=opis, podatki=podatki)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
