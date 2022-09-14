import mysql.connector

def lentokenttienlkm(maakoodi):
    sql = f'''select airport.type
    from airport
    where iso_country = "{maakoodi}"'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        small = 0
        medium = 0
        large = 0
        heliport = 0
        closed = 0
        seabase = 0
        balloonport = 0
        for i in tulos:
            for tyyppi in i:
                if tyyppi == "small_airport":
                    small += 1
                elif tyyppi == "medium_airport":
                    medium += 1
                elif tyyppi == "large_airport":
                    large += 1
                elif tyyppi == "heliport":
                    heliport += 1
                elif tyyppi == "closed":
                    closed += 1
                elif tyyppi == "seabase":
                    seabase += 1
                elif tyyppi == "balloonport":
                    balloonport += 1
                else:
                    continue

        print(f'''Pieniä lentokenttiä: {small}\n
        Keskikokoisia lentokenttiä: {medium}\n
        Isoja lentokenttiä: {large}\n
        Heliportteja: {heliport}
        Suljettuja: {closed}
        Seabaseja: {seabase}
        Balloonportteja: {balloonport}''')

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='0232',
    autocommit=True
)

koodi = input('Anna maakoodi: ')
lentokenttienlkm(koodi.upper())

# Vaihtoehtoinen, jälleen elegantimpi tapa:

def tyypit():
    sql = f'''select distinct type
    from airport'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def lentokenttienlkm2(maakoodi, tyyppi):
    sql = f'''select count(*)
    from airport
    where iso_country = "{maakoodi}"
    and type = "{tyyppi}";'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos2 = kursori.fetchone()
    return tulos2

koodi2 = input('Anna maakoodi: ')


for tyyppi in tyypit():
    print(lentokenttienlkm2(koodi2, tyyppi[0])[0], tyyppi[0])