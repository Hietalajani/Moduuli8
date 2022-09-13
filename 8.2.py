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
                else:
                    continue

        print(f'''Pieniä lentokenttiä: {small}\n
        Keskikokoisia lentokenttiä: {medium}\n
        Isoja lentokenttiä: {large}\n
        Heliportteja: {heliport}''')

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

def lentokenttienlkm2(maakoodi):
    sql = f'''select type, count(*)
    from airport
    where iso_country = "{maakoodi}"
    group by airport.type;'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print(f'''Maassa on lentokentätyyppejä:
        Suljettuja: {tulos[0][1]}
        Heliportteja: {tulos[1][1]}
        Suuria lentokenttiä: {tulos[2][1]}
        Keskikokoisia lentokenttiä: {tulos[3][1]}
        Pieniä lentokenttiä: {tulos[4][1]}.''')

koodi2 = input('Anna maakoodi: ')
lentokenttienlkm2(koodi2.upper())