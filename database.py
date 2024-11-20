# Imports
import os
from sqlalchemy import create_engine, text

connection_string = os.getenv('GRAFIS_PG_CONN_STR')

# Database
engine = create_engine(connection_string)

def load_gesla(iskalnik):
    q = '%' + iskalnik['q'] + '%'

    if iskalnik['q'] == '*':
        select = 'select * from slovarfizika order by geslo_slo'
    else:
        select = 'select * from slovarfizika where '
        geslo_slo = 'geslo_slo like :najdi '
        definicija_slo = 'definicija_slo like :najdi '
        geslo_ang = 'geslo_ang like :najdi ' 
        definicija_ang = 'definicija_ang like :najdi order by geslo_slo'
        select += geslo_slo + ' OR ' + definicija_slo + ' OR ' + geslo_ang + ' OR ' + definicija_ang

    with engine.connect() as conn:
        result = conn.execute(text(select), parameters=dict(najdi=q))
        rows = []
        for row in result.all():
           rows.append(row._mapping)
    return rows

#gesla = load_gesla({'q':'vpoj'})
#print(gesla)

def load_geslo(id):
    select = 'select * from slovarfizika where id = :val'
    with engine.connect() as conn:
        result = conn.execute(text(select), parameters=dict(val=id))
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._mapping
        
def import_data():
    with open('podatki.txt', encoding='UTF-8') as vhodna:
        for vrstica in vhodna:
            vrstica = vrstica.strip('\n')
            vrstica = vrstica.strip('\\')
            podatki = vrstica.split('&')
            geslo_ang = podatki[0].strip()
            geslo_slo = podatki[1].strip()
            definicija_ang = podatki[2].strip()
            definicija_slo = podatki[3].strip()
            iso = podatki[4].strip('')
            formula = ''
            oznaka = ''
            enota = ''
            opombe = ''            
            select = f"""insert into slovarfizika (
                            geslo_ang, 
                            geslo_slo, 
                            definicija_ang, 
                            definicija_slo, 
                            iso, 
                            formula, 
                            oznaka, 
                            enota, 
                            opombe)
                        values (
                            '{geslo_ang}',
                            '{geslo_slo}',
                            '{definicija_ang}',
                            '{definicija_slo}',
                            '{iso}',
                            '{formula}',
                            '{oznaka}',
                            '{enota}',
                            '{opombe}'
                            )
                    """
            with engine.connect() as conn:
                result = conn.execute(text(select))
                conn.commit()

def create_slovar_fizika():
    select =  '''create table slovarfizika (
                               id serial primary key,
                               geslo_ang varchar(100), 
                               geslo_slo varchar(100), 
                               definicija_ang varchar(1000), 
                               definicija_slo varchar(1000), 
                               iso varchar(100), 
                               formula varchar(300), 
                               oznaka varchar(10), 
                               enota varchar(10), 
                               opombe varchar(1000))'''
    with engine.connect() as conn:
          result = conn.execute(text(select))

#print('test')

#create_slovar_fizika()
#import_data()
#print(load_gesla())
#print(load_geslo(48))
