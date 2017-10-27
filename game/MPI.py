from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import hashlib
import time
import requests
import json
import random
from datetime import datetime

# Geeft aan dat het antwoord goed is met een popup
def goed_antwoord_PopUp():
    goed_antwoord_text = "Dat is het juiste antwoord!"
    toplevel = Toplevel()
    goed_antwoord_label = Label(toplevel, text=goed_antwoord_text, height=5, width=50).pack()
    sluit_popup = Button(toplevel, text="Woohoo!", command=toplevel.destroy).place(x=175, y=59)
    toplevel.resizable(0, 0)


# Pop up voor de highscores scherm
def highscore_popup():
    mt = Toplevel()
    mt.geometry("1000x580")

    tree = ttk.Treeview(mt)

    tree['columns'] = (0, 1, 2)
    tree['show'] = 'headings'
    tree.column(0)
    tree.heading(0, text="Name")
    tree.column(1)
    tree.heading(1, text="Score")
    tree.column(2)
    tree.heading(2, text="Datetime")

    for key, user in score_ophalen().items():
        tree.insert("", 0, user['name'], values=(user['name'], user['score'], user['datetime']))
    tree.pack(fill="both")
    Label(toplevel, text="highscore", height=20, width=70).pack()
    Button(toplevel, text="Sluit venster", command=toplevel.destroy).place(x=350, y=120)
    toplevel.resizable(0, 0)


# Brengt de speler naar het game-over scherm zodra hij 0 punten heeft.
def game_over_scherm():
    global achtergrond, label_achtergrond
    file = PhotoImage(file="gameover_scherm.gif")
    label = Label(root, image=file).place(x=0, y=0, relwidth=1, relheight=1)


# Deze functie laat een pop up zien waarin de speler succes toegewenst wordt
def succes_PopUp():
    succes_tekst = "Succes met de uitdaging, " + str(entry_box.get().capitalize()) + "!"
    toplevel = Toplevel()
    succes_popup_label = Label(toplevel, text=succes_tekst, height=5, width=50).pack()
    sluit_popup = Button(toplevel, text="Dankjewel!", command=toplevel.destroy).place(x=175, y=59)
    toplevel.resizable(0, 0)


# Deze functie geeft een foutmelding aan de gebruiker wanneer die een ongeldige naam invoert
def ongeldige_naam_PopUp():
    ongeldige_naam = "Voer een geldige naam in, een naam moet minimaal 1 karakter bevatten en maximaal 15."
    toplevel = Toplevel()
    ongeldige_naam_label = Label(toplevel, text=ongeldige_naam, height=5, width=65).pack()
    sluit_PopUp = Button(toplevel, text="Begrepen.", command=toplevel.destroy).place(x=250, y=59)
    toplevel.resizable(0, 0)


# Deze functie maakt het mogelijk om een hint te vragen
def hint_PopUp(hint):
    toplevel = Toplevel()
    hint_label = Label(toplevel, text=hint, height=5, width=65).pack()
    sluit_PopUp = Button(toplevel, text="Dankjewel voor de hint.", command=toplevel.destroy).place(x=250, y=59)
    #toplevel.resizable(0, 0)


# Deze functie geeft een gratis hint om te beginnen met raden
def gratis_hint_PopUp(superheld):
    print(superheld)
    hint = beschrijvinghint(superheld)
    toplevel=Toplevel()
    gratis_hint_label = Label(toplevel, text=hint, height=5, width=65).pack()
    sluit_PopUp = Button(toplevel, text="Dankjewel voor de gratis hint.", command=toplevel.destroy).place(x=250, y=59)
    toplevel.resizable(0, 0)


# Deze functie brengt de speler naar het volgende scherm, achtergrond en de startknop
def tweede_scherm():
    global achtergrond, label_achtergrond, canvas, gebruikersnaam, entry_box
    canvas = Canvas(root, height=650, width=500).pack()
    achtergrond = PhotoImage(file="tweede_achtergrond.gif")
    label_achtergrond = Label(root, image=achtergrond)
    label_achtergrond.place(x=0, y=0, relwidth=1, relheight=1)

    # Vragen naar de naam van de speler en creëren van de start knop
    naam_vraag = Label(root, text="Naam:", font=("arial", 17, "bold"), bg="gray9", fg="red").place(x=4, y=117)
    entry_box = Entry(root, width=18, bg="dark slate gray")
    entry_box.place(x=60, y=116)
    start_button = Button(root, text="Start", width=5, height=1, command=derde_scherm).place(x=61, y=150)
    quit = Button(root, font=("arial", 10, "bold"), bg="gray9", fg="red", text="Quit", width=15,
                  command=root.destroy).place(x=533, y=479)


# Creatie van het derde scherm en van de opties waar de speler uit kan kiezen
def derde_scherm():
    global entry_box, achtergrond, label_achtergrond, gebruikersnaam

    # Als de speler een ongeldige naam invoert, start het spel niet
    if entry_box.get() is "" or len(entry_box.get()) > 15:
        ongeldige_naam_PopUp()
    # Creatie van het starten van het spel en het spelen
    else:

        gebruikersnaam = entry_box.get()
        antwoord = willekeurigeheld(True)
        succes_PopUp()
        achtergrond = PhotoImage(file="derde_achtergrond.gif")
        label_achtergrond = Label(root, image=achtergrond).place(x=0, y=0, relwidth=1, relheight=1)
        punten_label = Label(root, font=("arial", 15, "bold"), bg="white", text="Punten: " + str(punten)).place(x=10,
                                                                                                                y=150)
        # while True:
        gratis_hint_button = Button(label_achtergrond, text="Gratis hint!", command=lambda: gratis_hint_PopUp(antwoord)).place(x=20, y=185)

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
        # De opties waar speler uit kan kiezen.
        for answer in antwoorden:
            Radiobutton(label_achtergrond, text=answer, value=answer, variable=gok).place(x=20, y=(225 + index * 25))
            index += 1

        # Creatie van de 'Hint Button' die de speler een hint geeft ten koste van 3 punten
        hint_button = Button(label_achtergrond, font=("arial", 9, "bold"), fg="OrangeRed3",
                             command=lambda: hintophalen(antwoord),
                             text="HINT(-3 punten)").place(x=462, y=250)
        # Creatie van de button die de keuze van de speler bevestigt
        ok_button = Button(label_achtergrond, font=("arial", 9, "bold"),
                           command=lambda: check_antwoord(gok.get(), antwoord),
                           text="BEVESTIGEN").place(x=150, y=450)
        # Creatie van de button om de highscores te laten zien
        print(gebruikersnaam, punten)
        highscore_button = Button(label_achtergrond, text="highscore", command=highscore_popup).place(x=500, y=40)
        quit = Button(root, font=("arial", 10, "bold"), bg="gray9", fg="red", text="Quit", command=lambda: spel_stoppen(gebruikersnaam, punten), width=15,
                      ).place(x=533, y=472)


# Haal highscores op.
def score_ophalen():
    dict = {}
    with open('highscore.txt', 'r') as file:
        index = 0
        for line in file:
            parts = line.split(',')
            dict[index] = {}
            dict[index]['name'] = parts[0]
            dict[index]['score'] = parts[1]
            dict[index]['datetime'] = parts[2]
            index += 1

    return dict


# Kijk of het antwoord goed was.
def check_antwoord(gok, antwoord):
    global punten
    print(gok, antwoord['name'])
    if gok == antwoord['name']:
        punten += 25
        goed_antwoord_PopUp()
        derde_scherm()
    else:
        punten -= 1


# Deze fucntie helpt bij het opbouwen van de url.
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


# Haal alle helden op uit de Marvel API.
def allehelden():
    response = requests.get(querybuilder("characters", False, False))
    resultaat = json.loads(response.text)

    return resultaat


# Haalt een willekeurige held op uit de Marvel API.
def willekeurigeheld(beschrijving=False, offset=1):
    willekeuriggetal = random.randrange(0, allehelden()["data"]["total"])
    response = requests.get(querybuilder("characters", willekeuriggetal, offset))
    resultaat = json.loads(response.text)

    held = resultaat["data"]["results"][0]
    if beschrijving:
        if held["description"] == "":
            return willekeurigeheld()
        else:
            return held
    else:
        return held


# Roept de juiste hintfuncite op
def hintophalen(superheld):
    randhint = random.randrange(1, 4)

    if randhint == 1:
        hint = comichint(superheld)['name']
    elif randhint == 2:
        hint = eventshint(superheld)['name']
    elif randhint == 3:
        hint = serieshint(superheld)['name']

    if hint:
        global punten
        punten -= 3
        hint_PopUp(hint)
    else:
        return hintophalen(superheld)


# Een hint met de comci waarin de held zit.
def comichint(superheld):
    if superheld["comics"]["returned"] > 0:
        randomnumber = random.randrange(0, superheld["comics"]["returned"])

        return superheld["comics"]["items"][randomnumber]

    return False


# Een beschrijving van de held.
def beschrijvinghint(superheld):
    if superheld["description"]:
        return superheld["description"]

    return False


# Haal serie hint op.
def serieshint(superheld):
    if superheld["series"]["returned"] > 0:
        randomnumber = random.randrange(0, superheld["series"]["returned"])

        return superheld["series"]["items"][randomnumber]

    return False


# Haal hint op met de events waar de held in zat.
def eventshint(superheld):
    if superheld["events"]["returned"] > 0:
        randomnumber = random.randrange(0, superheld["events"]["returned"])

        return superheld["events"]["items"][randomnumber]

    return False


# Voeg een score toe aan de highscores.
def scoretoevoegen(gebruikersnaam, punten):
    tijd = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
    string = ','.join([gebruikersnaam, str(punten), tijd])
    print(string)
    with open('highscore.txt', 'a') as file:
        file.write(string + '\n')


# Stop het spel.
def spel_stoppen(gebruikersnaam, punten):
    scoretoevoegen(gebruikersnaam, punten)
    root.destroy()


# Maken van het Tkinter window
root = Tk()
entry_box = Entry()

# Het aantal punten waar elke speler mee start
punten = 0
gebruikersnaam = ""
canvas = Canvas(root, height=0, width=500)

achtergrond = PhotoImage(file="beginscherm.gif")

label_achtergrond = Label(root, image=achtergrond)
label_achtergrond.place(x=1, y=0, relwidth=1, relheight=0.85)

button = Button(root, font=("arial", 25, "bold"), fg="yellow2", text="Ben je er klaar voor?", bg="hot pink",
                command=tweede_scherm)

# Creatie van de button om de applicatie af te sluiten; "quit"
quit = Button(root, font=("arial", 10, "bold"), bg="red", fg="red", text="Quit", width=15, command=root.destroy).place(
    x=533, y=479)

button.pack(side="bottom")

root.title("SuperWonderCaptain")
root.geometry("650x500")
root.resizable(0, 0)

canvas.pack()

root.mainloop()
