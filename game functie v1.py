import json
import random
import requests
import tkinter


def game():
    punten = 25
    superheld = input("Welke superheld is het")
    naam = input("Welke superheld gok je")


    while naam != superheld:
        print("foute held")
        punten = punten -1
        naam = input("welke superheld gok je")

    print("Uw verdiende punten voor deze ronde zijn: " + str(punten))
    global totaalpunten
    totaalpunten = totaalpunten + punten
    print("Uw totale punten zijn: " + str(totaalpunten))

    stoppen = input("wil je doorgaan")
    while stoppen != "stop":
        superheld = input("Welke superheld is het")
        naam = input("Welke superheld gok je")

        while naam != superheld:
            print("foute held")
            punten = punten - 1
            naam = input("welke superheld gok je")

        print("Uw verdiende punten voor deze ronde zijn: " + str(punten))
        totaalpunten = totaalpunten + punten
        print("Uw totale punten zijn: " + str(totaalpunten))
        stoppen = input("wilt u stoppen")

    print("Beste " + naamgebruiker + ", uw totaalscore is " + str(totaalpunten) + "! Dit wordt opgeslagen")

naamgebruiker = input("Voer je naam in:")
totaalpunten = 0

game()


print("Beste " + naamgebruiker + ", uw totaalscore is " + str(totaalpunten) + "! Dit wordt opgeslagen")

nieuwegebruiker = input("Wil iemand anders spelen?")
while nieuwegebruiker == "ja":
    naamgebruiker = input("Wat is je naam")
    totaalpunten = 0
    game()

    nieuwegebruiker = input("wilt iemand anders spelen")


