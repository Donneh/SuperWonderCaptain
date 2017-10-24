import hashlib
import time
import requests
import json
import random
from datetime import datetime, timedelta


def scoretoevoegen(naam, punten):
    tijd = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
    string = ','.join([naam, str(punten), tijd])

    with open('highscore.txt', 'a') as file:
        file.write(string + '\n')


def hintophalen(superheld):
    return "De hint is: " + superheld['name']

def querybuilder(query, offset, limit):
    ts = str(time.time())
    base_url = "http://gateway.marvel.com:80/v1/public/"
    private_key = "06ee96159e2ca9e3e1a9c4a24a3ff3beb84e0f29"
    public_key = "e6980fd5a2c64c097524fec491b506a9"
    hashed = hashlib.md5((ts + private_key + public_key).encode('utf-8'))
    md5digest = str(hashed.hexdigest())
    if offset:
        return base_url + query + "?offset=" + str(offset) + "&limit=" + str(limit) + "&ts=" + ts + "&apikey=" + public_key + "&hash=" + md5digest

    return base_url + query + "?ts=" + ts + "&apikey=" + public_key + "&hash=" + md5digest


def allehelden():
    response = requests.get(querybuilder("characters", False, False))
    resultaat = json.loads(response.text)

    return resultaat


def willekeurigeheld():
    willekeuriggetal = random.randrange(0, allehelden()["data"]["total"])
    response = requests.get(querybuilder("characters", willekeuriggetal, 1))
    resultaat = json.loads(response.text)

    return resultaat


def game():
    naamgebruiker = input("Voer je naam in:")
    stoppen = input("wil je stoppen")
    totaalpunten = 0

    # In deze while loop blijft het programma vragen naar een nieuwe superheld tot dat stop in wordt gevoerd
    while stoppen != "stop":
        punten = 25
        superheld = willekeurigeheld()["data"]["results"][0]
        antwoord = superheld["name"]
        print(hintophalen(superheld))
        naam = input("Welke superheld gok je")

        # in deze while loop blijft het programma naar dezelfde superheld vragen als je het niet goed raad
        while naam != antwoord:
            print("foute held")
            punten = punten - 1
            if input("Wil je een hint? (y/n)") == "y":
                print(hintophalen(superheld))
                punten -= 3
            naam = input("welke superheld gok je")

        print("Uw verdiende punten voor deze ronde zijn: " + str(punten))
        totaalpunten = totaalpunten + punten
        print("Uw totale punten zijn: " + str(totaalpunten))
        stoppen = input("wil je stoppen")

    # hier worden de punten opgeslagen naar een bestand
    scoretoevoegen(naamgebruiker, totaalpunten)
    print("Beste " + naamgebruiker + ", uw totaalscore is " + str(totaalpunten) + "! Dit wordt opgeslagen")


def nieuwegebruiker():
    nieuwegebruiker = input("Wil iemand anders spelen?")

    # Indien er een volgende gebruiker wilt spelen wordt de game functie benut
    while nieuwegebruiker == "ja":
        game()
        nieuwegebruiker = input("wilt iemand anders spelen")


game()
nieuwegebruiker()
