# Imports
import os
from sqlalchemy import create_engine, text

connection_string = os.getenv('GRAFIS_PG_CONN_STR')

# Database
engine = create_engine(connection_string)

def load_gesla():
    with engine.connect() as conn:
        result = conn.execute(text('select * from slovar'))
        rows = []
        for row in result.all():
           rows.append(row._mapping)
    return rows

#print(load_gesla())