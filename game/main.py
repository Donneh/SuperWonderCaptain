import hashlib
import time
import requests
import json
import random
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image


# Deze functie brengt de speler naar het volgende scherm, achtergrond en de startknop
def speler_aanmaak_scherm():
    global achtergrond, label_achtergrond, canvas, naam, entry_box

    canvas = Canvas(root, height=650, width=500).pack()
    achtergrond = PhotoImage(file="tweede_achtergrond.gif")
    label_achtergrond = Label(root, image=achtergrond)
    label_achtergrond.place(x=0, y=0, relwidth=1, relheight=1)


    # Vragen naar de naam van de speler en creëren van de start knop
    Label(root, text="Naam:", font=("arial", 17, "bold"), bg="gray9", fg="red").place(x=4, y=117)
    entry_box = Entry(root, width=18, bg="dark slate gray")
    entry_box.place(x=60, y=118)
    Button(root, text="Start", width=5, height=1, command=vraag_scherm).place(x=60, y=143)


# Creatie van het derde scherm en van de opties waar de speler uit kan kiezen
def vraag_scherm():
    global entry_box, achtergrond, label_achtergrond, antwoord

    # Als de speler een ongeldige naam invoert, start het spel niet
    if entry_box.get() is "":
        print("Voer een geldige naam in.")

    # Creatie van het starten van het spel en het spelen
    else:
        print("Succes met de uitdaging, " + str(entry_box.get().capitalize()) + "!")
        achtergrond = PhotoImage(file="derde_achtergrond.gif")
        label_achtergrond = Label(root, image=achtergrond).place(x=0, y=0, relwidth=1, relheight=1)
        punten_label = Label(root, font=("arial", 15, "bold"), bg="white", text="Punten: " + str(punten)).place(x=10, y=150)

        antwoorden = [
            antwoord['name'],
            willekeurigeheld()['name'],
            willekeurigeheld()['name'],
            willekeurigeheld()['name'],
            willekeurigeheld()['name'],
            willekeurigeheld()['name'],
            willekeurigeheld()['name'],
            willekeurigeheld()['name'],
            willekeurigeheld()['name'],
            willekeurigeheld()['name']
        ]
        print(antwoord['name'])

        random.shuffle(antwoorden)
        index = 0
        gok = StringVar()
        for answer in antwoorden:
            Radiobutton(label_achtergrond, text=answer, value=answer, variable=gok).place(x=20, y=(225 + index * 25))
            index += 1
        ok_button = Button(label_achtergrond, font=("arial", 9, "bold"), text="BEVESTIGEN", command=lambda: check_antwoord(gok.get())).place(x=250, y=250)

        hint_button = Button(label_achtergrond, font=("arial", 9, "bold"), fg="OrangeRed3", text="Hint(-3 punten").place(x=462, y=450)



def check_antwoord(gok):
    global antwoord, punten
    print(antwoord["name"], gok)
    if antwoord["name"] == gok:
        punten += 25
        print("Goede antwoord")
        vraag_scherm()

    return False


def scoretoevoegen(naam, punten):
    tijd = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
    string = ','.join([naam, str(punten), tijd])

    with open('highscore.txt', 'a') as file:
        file.write(string + '\n')


def hintophalen(superheld):
    print("1: beschrijving")
    print("2: Comic hint")
    print("3: Events hint")
    print("4: Series hint")
    antwoord = int(input("Welk soort hint wil je? "))
    if antwoord == 1:
        hint = beschrijvinghint(superheld)
    elif antwoord == 2:
        hint = comichint(superheld)['name']
    elif antwoord == 3:
        hint = eventshint(superheld)['name']
    elif antwoord == 4:
        hint = serieshint(superheld)['name']

    if hint:
        return hint
    else:
        print("Deze hint is niet beschikbaar, kies opnieuw")
        hintophalen(superheld)


def comichint(superheld):
    if superheld["comics"]["returned"] > 0:
        randomnumber = random.randrange(0, superheld["comics"]["returned"])

        return superheld["comics"]["items"][randomnumber]

    return False


def beschrijvinghint(superheld):
    if superheld["description"]:
        return superheld["description"]

    return False


def serieshint(superheld):
    if superheld["series"]["returned"] > 0:
        randomnumber = random.randrange(0, superheld["series"]["returned"])

        return superheld["series"]["items"][randomnumber]

    return False


def eventshint(superheld):
    if superheld["events"]["returned"] > 0:
        randomnumber = random.randrange(0, superheld["events"]["returned"])

        return superheld["events"]["items"][randomnumber]

    return False


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


def willekeurigeheld(beschrijving=False):
    willekeuriggetal = random.randrange(0, allehelden()["data"]["total"])
    response = requests.get(querybuilder("characters", willekeuriggetal, 1))
    resultaat = json.loads(response.text)

    held = resultaat["data"]["results"][0]

    if beschrijving:
        if held["description"] != "":
            return held
        else:
            return willekeurigeheld()
    else:
        return held


def game():
    naamgebruiker = input("Voer je naam in:")
    stoppen = input("wil je stoppen")
    totaalpunten = 0

    # In deze while loop blijft het programma vragen naar een nieuwe superheld tot dat stop in wordt gevoerd
    while stoppen != "stop":
        punten = 25
        superheld = willekeurigeheld()
        antwoord = superheld["name"]
        print(antwoord)
        print(beschrijvinghint(superheld))

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



# Maken van het Tkinter window
root = Tk()
entry_box = Entry()
canvas = Canvas(root, height=0, width=500)

achtergrond = PhotoImage(file="beginscherm.gif")
label_achtergrond = Label(root, image=achtergrond)
label_achtergrond.place(x=1, y=0, relwidth=1, relheight=0.85)

# Het aantal punten waar elke speler mee start
punten = 0

button = Button(root, font=("arial", 25, "bold"), fg="yellow2", text="Ben je er klaar voor?", bg="hot pink",
                command=speler_aanmaak_scherm)
button.pack(side="bottom")

root.title("SuperWonderCaptain")
root.geometry("650x500")
root.resizable(0, 0)

canvas.pack()

root.mainloop()
