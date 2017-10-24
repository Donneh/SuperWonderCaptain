def game():
    naamgebruiker = input("Voer je naam in:")
    stoppen = input("wil je stoppen")
    totaalpunten = 0

    # In deze while loop blijft het programma vragen naar een nieuwe superheld tot dat stop in wordt gevoerd
    while stoppen != "stop":
        punten = 25
        superheld = input("Welke superheld is het")
        naam = input("Welke superheld gok je")

        # in deze while loop blijft het programma naar dezelfde superheld vragen als je het niet goed raad
        while naam != superheld:
            print("foute held")
            punten = punten - 1
            naam = input("welke superheld gok je")

        print("Uw verdiende punten voor deze ronde zijn: " + str(punten))
        totaalpunten = totaalpunten + punten
        print("Uw totale punten zijn: " + str(totaalpunten))
        stoppen = input("wil je stoppen")

    # hier worden de punten opgeslagen naar een bestand
    print("Beste " + naamgebruiker + ", uw totaalscore is " + str(totaalpunten) + "! Dit wordt opgeslagen")

def nieuwegebruiker():
    nieuwegebruiker = input("Wil iemand anders spelen?")

    # Indien er een volgende gebruiker wilt spelen wordt de game functie benut
    while nieuwegebruiker == "ja":
        game()
        nieuwegebruiker = input("wilt iemand anders spelen")
game()
nieuwegebruiker()
