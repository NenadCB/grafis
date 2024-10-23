from flask import Flask, render_template

app = Flask(__name__)

geslo = 'sila'
opis = 'sila je moja najljubša igra'

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://grafis_owner:RTogb40WyXmG@ep-autumn-sunset-a8e3slx5.eastus2.azure.neon.tech/grafis?sslmode=require"

# Database
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('home.html', geslo=geslo, opis=opis)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
