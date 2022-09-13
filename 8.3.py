import mysql.connector
from geopy import distance

def etäisyys(piste1, piste2):
    sql = f'''select latitude_deg, longitude_deg
    from airport
    where ident = "{piste1}" or ident = "{piste2}";'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
    if kursori.rowcount > 1:
        airport1 = (tulos[0][0], tulos[0][1])
        airport2 = (tulos[1][0], tulos[1][1])
        print(f'Lentokenttien välinen matka on {distance.distance(airport1, airport2).km:.2f} kilometriä.')

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='0232',
    autocommit=True
)

koodit = []
for i in range(2):
    koodi = input(f'Anna {i+1}. lentokentän ICAO-koodi: ')
    koodit.append(koodi.upper())

etäisyys(koodit[0], koodit[1])