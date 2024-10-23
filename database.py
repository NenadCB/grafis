# Imports
from flask import (
  Flask,
  abort,
  redirect,
  url_for,
  render_template,
  make_response
)

from sqlalchemy import create_engine, text

# Database
engine = create_engine("postgresql://grafis_owner:RTogb40WyXmG@ep-autumn-sunset-a8e3slx5.eastus2.azure.neon.tech/grafis?options=endpoint%3Dep-autumn-sunset-a8e3slx5"
)


with engine.connect() as conn:
    result = conn.execute(text('select * from slovar'))
    print(result.all())