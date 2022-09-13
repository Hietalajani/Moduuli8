import mysql.connector

def haekenttä(ICAO):
    sql = f'''select airport.name, airport.municipality 
    from airport 
    where ident = "{ICAO}";'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print(f'Lentokentän nimi on {tulos[0][0]} ja paikkakunta {tulos[0][1]}.')
    return

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='0232',
    autocommit=True
)

tunnus = input('Anna lentokentän ICAO-koodi: ')
haekenttä(tunnus)